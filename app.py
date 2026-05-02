import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from scorer import RelevanceScorer
from metrics import SearchMetrics
from classifier import QueryClassifier
from sample_data import get_sample_data

st.set_page_config(page_title="AI Search Relevance Tester", page_icon="🔍", layout="wide")

st.title("🔍 AI Search Relevance Tester")
st.markdown("**NLP-Powered Search Quality Evaluation** — Score relevance, detect failures, get PM recommendations.")
st.markdown("---")

# Sidebar
st.sidebar.header("⚙️ Configuration")
scoring_mode = st.sidebar.selectbox("Scoring Mode", ["TF-IDF (Lexical)", "Semantic (Embeddings)"])
k_positions = st.sidebar.slider("Evaluate top K results", min_value=3, max_value=10, value=5)
relevance_threshold = st.sidebar.slider("Relevance threshold (0-1)", min_value=0.1, max_value=0.9, value=0.4, step=0.05)

st.sidebar.markdown("---")
st.sidebar.markdown("**Metrics computed:** NDCG@K, MRR, Precision@1, Coverage")

# Data input
st.header("📥 Query-Result Data")
data_source = st.radio("Data source", ["Use sample dataset (SaaS PM tool)", "Upload CSV"])

if data_source == "Use sample dataset (SaaS PM tool)":
      data = get_sample_data()
      st.success(f"Loaded {len(data['queries'])} queries with {k_positions} results each.")
else:
      uploaded = st.file_uploader("Upload CSV (columns: query, result_title, result_content, relevance_label)", type="csv")
      if uploaded:
                df = pd.read_csv(uploaded)
                st.dataframe(df.head())
                data = {"queries": [], "results": [], "labels": []}
                for query, group in df.groupby("query"):
                              data["queries"].append(query)
                              data["results"].append(group[["result_title", "result_content"]].to_dict("records"))
                              data["labels"].append(group["relevance_label"].tolist())
      else:
                st.info("Upload a CSV or use the sample dataset.")
                st.stop()

  if st.button("🔍 Run Search Quality Evaluation", type="primary"):
        scorer = RelevanceScorer(mode="tfidf" if "TF-IDF" in scoring_mode else "semantic")
        metrics_calc = SearchMetrics(k=k_positions)
        classifier = QueryClassifier()

    results_data = []
    all_ndcg, all_mrr, all_p1 = [], [], []

    with st.spinner("Evaluating search quality..."):
              for i, query in enumerate(data["queries"]):
                            query_type = classifier.classify(query)
                            results = data["results"][i]
                            labels = data["labels"][i]

                  # Score relevance for each result
                            scores = scorer.score(query, results)

                  # Calculate metrics
                            ndcg = metrics_calc.ndcg(labels, scores)
                            mrr = metrics_calc.mrr(labels)
                            p1 = 1 if labels[0] >= 2 else 0  # Position 1 relevant if label >= 2

            all_ndcg.append(ndcg)
            all_mrr.append(mrr)
            all_p1.append(p1)

            # Detect ranking failure
            top_score = scores[0] if scores else 0
            failure = top_score < relevance_threshold and labels[0] < 2

            results_data.append({
                              "Query": query,
                              "Type": query_type,
                              "NDCG@K": round(ndcg, 3),
                              "MRR": round(mrr, 3),
                              "P@1": "✅" if p1 else "❌",
                              "Top Score": round(top_score, 3),
                              "Status": "🚨 Failure" if failure else ("⚠️ Warning" if ndcg < 0.65 else "✅ Good"),
            })

    # Summary metrics
    st.markdown("---")
    st.header("📊 Search Quality Report")

    m1, m2, m3, m4 = st.columns(4)
    avg_ndcg = np.mean(all_ndcg)
    avg_mrr = np.mean(all_mrr)
    avg_p1 = np.mean(all_p1)
    quality_score = (avg_ndcg * 0.4 + avg_mrr * 0.3 + avg_p1 * 0.3) * 100

    m1.metric("Overall Quality Score", f"{quality_score:.1f}/100", delta="Target: 85+")
    m2.metric(f"NDCG@{k_positions}", f"{avg_ndcg:.3f}", delta="Target: >0.85")
    m3.metric("MRR", f"{avg_mrr:.3f}", delta="Target: >0.90")
    m4.metric("Precision@1", f"{avg_p1*100:.0f}%", delta="Target: >80%")

    # Results table
    results_df = pd.DataFrame(results_data)
    st.subheader("Per-Query Results")

    def highlight_failures(row):
              if "🚨" in str(row.get("Status", "")):
                            return ["background-color: #ffcccc"] * len(row)
elif "⚠️" in str(row.get("Status", "")):
            return ["background-color: #fff3cd"] * len(row)
        return [""] * len(row)

    st.dataframe(results_df.style.apply(highlight_failures, axis=1), use_container_width=True)

    # NDCG chart
    fig = go.Figure()
    fig.add_bar(x=results_df["Query"], y=results_df["NDCG@K"], name="NDCG@K",
                                marker_color=["red" if v < 0.5 else "orange" if v < 0.7 else "green" for v in results_df["NDCG@K"]])
    fig.add_hline(y=0.85, line_dash="dash", line_color="blue", annotation_text="Target (0.85)")
    fig.update_layout(title=f"NDCG@{k_positions} by Query", xaxis_tickangle=-30, height=350)
    st.plotly_chart(fig, use_container_width=True)

    # PM Recommendations
    st.markdown("---")
    st.header("💡 PM Recommendations")
    failures = results_df[results_df["Status"].str.contains("Failure|Warning")]
    if not failures.empty:
              for _, row in failures.iterrows():
                            severity = "🚨" if "Failure" in row["Status"] else "⚠️"
                            with st.expander(f"{severity} Query: '{row['Query']}' — NDCG: {row['NDCG@K']} | Type: {row['Type']}"):
                                              if row["Type"] == "Transactional":
                                                                    st.markdown("**Root cause:** Transactional queries (action verbs) may return documentation instead of feature pages. Check if your index prioritizes content pages over UI actions.")
                                                                    st.markdown("**Recommendation:** Add feature-action synonyms to your index; boost results matching action verbs.")
    elif row["Type"] == "Navigational":
                          st.markdown("**Root cause:** Navigational queries expect an exact match to a specific page/feature. Poor P@1 suggests the right page is not ranked first.")
                          st.markdown("**Recommendation:** Audit your index for the specific entity the user is searching for. Consider exact-match boosting for navigational queries.")
else:
                      st.markdown("**Root cause:** Informational queries require comprehensive coverage. Low NDCG may indicate vocabulary mismatch (user's terms vs. indexed terms).")
                      st.markdown("**Recommendation:** Add synonym expansion, concept mapping, or consider semantic search for informational queries.")
else:
        st.success("No critical failures detected. Search quality is above threshold for all queries!")

    st.caption("AI Search Relevance Tester | [GitHub](https://github.com/Poojaahegde/ai-search-relevance-tester)")
