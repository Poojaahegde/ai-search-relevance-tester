# AI Search Relevance Tester 🔍 — NLP-Powered Search Quality Evaluation

Stop shipping bad search. Measure query-result relevance with NLP, detect ranking failures, and get PM-ready recommendations — before users notice.

## 🚀 Product Overview

### The Problem
Search is the highest-intent feature in most products — and the hardest to evaluate. PMs ship "improved search" without knowing if it actually works. The problem: relevance is subjective, hard to measure, and varies by query type. Without a systematic evaluation framework, PMs are flying blind on one of their most critical features.

Teams commonly ship search changes that regress specific query types (head queries improve, tail queries break), introduce ranking failures (irrelevant results in position 1), or fail to serve navigational vs. informational queries differently — all without any detection system.

### The Solution
AI Search Relevance Tester takes a set of test queries + result sets, applies NLP similarity scoring (TF-IDF cosine similarity + semantic embeddings), detects ranking failures and relevance gaps, and generates a PM-readable quality report with prioritized improvement recommendations.

### The Impact
- 📐 **Scores search relevance** for any query-result pair using semantic NLP similarity
- - 🚨 **Detects ranking failures** — irrelevant results promoted to top positions
  - - 📊 **Generates NDCG, MRR, and Precision@K metrics** — the industry-standard search quality metrics
    - - 🔍 **Classifies query intent** (navigational, informational, transactional) to evaluate context-aware ranking
      - - 💡 **Produces PM-ready recommendations** prioritized by user impact
       
        - ---

        ## 🎯 Why This Matters (Product Perspective)

        Search PM is one of the most technical PM specializations — and one of the most in-demand. PMs who can reason about search quality metrics, evaluate relevance, and communicate search improvements to engineering have a significant edge.

        This tool demonstrates that I understand how search evaluation works at a technical level: not just "search feels better" but measurable NDCG improvement from 0.72 to 0.89, MRR improvement, and precision at rank 1 and 5.

        **The key insight:** Most PMs treat search quality as a user perception problem ("users complain about search"). This tool makes it measurable, systematic, and proactive.

        ---

        ## 🧠 AI/ML Explanation

        | Component | Technique | Why It Was Chosen |
        |---|---|---|
        | Relevance Scoring | TF-IDF Cosine Similarity | Fast, interpretable baseline — measures lexical overlap between query and result |
        | Semantic Similarity | Sentence-BERT embeddings (optional) | Captures semantic meaning, not just keyword overlap — handles synonyms and paraphrases |
        | Ranking Quality | NDCG (Normalized Discounted Cumulative Gain) | Industry-standard metric — weights relevance by position (top results matter more) |
        | Reciprocal Rank | MRR (Mean Reciprocal Rank) | Measures how quickly users find the first relevant result |
        | Query Classification | Rule-based + keyword heuristics | Separates navigational (find X), informational (learn about X), transactional (buy X) queries |
        | Failure Detection | Threshold anomaly detection | Flags positions where relevance score drops below baseline by >2 standard deviations |

        **Key Metrics:**
        - **NDCG@5**: Measures relevance of top 5 results, weighted by position (higher = better)
        - - **MRR**: Mean Reciprocal Rank — average of 1/rank of first relevant result
          - - **Precision@1**: Is the #1 result relevant? The most critical metric for search UX
            - - **Coverage**: % of queries where at least one relevant result appears in top 5
             
              - ---

              ## 🛠 Tech Stack

              | Layer | Technology |
              |---|---|
              | UI | Streamlit |
              | NLP (Lexical) | scikit-learn (TF-IDF, cosine similarity) |
              | NLP (Semantic) | sentence-transformers (optional, for richer scoring) |
              | Data Processing | Pandas, NumPy |
              | Visualization | Plotly (heatmaps, ranking charts) |
              | Language | Python 3.8+ |

              ---

              ## 📊 Sample Output

              **Test Dataset:** 10 queries, 5 results each, for a project management SaaS

              | Query | Query Type | NDCG@5 | MRR | P@1 | Status |
              |---|---|---|---|---|---|
              | "how to invite team members" | Informational | 0.91 | 1.00 | ✅ Relevant | Good |
              | "billing settings" | Navigational | 0.87 | 1.00 | ✅ Relevant | Good |
              | "export project to CSV" | Transactional | 0.43 | 0.50 | ❌ Irrelevant | 🚨 Failure |
              | "task dependencies" | Informational | 0.62 | 0.33 | ❌ Irrelevant | ⚠️ Warning |
              | "notification preferences" | Navigational | 0.78 | 1.00 | ✅ Relevant | Good |

              **Overall Search Quality Score: 72.4/100**
              - NDCG@5 (avg): 0.724 — Target: >0.85
              - - MRR (avg): 0.77 — Target: >0.90
                - - P@1 (avg): 60% — Target: >80%
                  - - Ranking Failures Detected: 3 queries
                   
                    - **Top PM Recommendations:**
                    - 1. 🚨 **Fix "export" query results** — transactional queries ("export to CSV") are returning documentation pages instead of the export feature. Root cause: index prioritizes content pages over feature pages for action verbs.
                      2. 2. ⚠️ **Improve tail query handling** — "task dependencies" shows poor relevance. Root cause: compound concept not in index vocabulary. Solution: add synonym expansion or concept mapping.
                         3. 3. 📈 **A/B test semantic search** — current lexical model struggles with paraphrase queries. Embedding model improves NDCG by estimated +0.12 on informational queries.
                           
                            4. ---
                           
                            5. ## 📸 Demo Instructions
                           
                            6. ```bash
                               # 1. Clone the repo
                               git clone https://github.com/Poojaahegde/ai-search-relevance-tester.git
                               cd ai-search-relevance-tester

                               # 2. Install dependencies
                               pip install -r requirements.txt

                               # 3. Launch the app
                               streamlit run app.py
                               ```

                               Open `http://localhost:8501` in your browser.

                               **Input options:**
                               - Use the built-in sample dataset (10 PM SaaS queries)
                               - - Upload your own CSV with columns: `query`, `result_title`, `result_content`, `relevance_label` (0-3)
                                 - - Paste query-result pairs directly in the UI
                                  
                                   - **Output:**
                                   - - Per-query relevance heatmap
                                     - - NDCG/MRR/P@K trend charts
                                       - - Ranking failure alerts
                                         - - PM recommendation report (downloadable)
                                          
                                           - ---

                                           ## 🎯 Product Thinking Layer

                                           ### 👥 Target Users
                                           - **Search PMs** evaluating ranking model changes before deployment
                                           - - **Product Managers** at content, e-commerce, or SaaS companies where search is a core feature
                                             - - **Growth PMs** using search quality as a leading indicator of user activation and retention
                                              
                                               - ### 😣 Pain Points Solved
                                               - - **"Search feels worse"** — vague user complaints with no measurement system to validate or disprove
                                                 - - **Blind search releases** — shipping ranking changes without knowing if specific query types regressed
                                                   - - **Inconsistent evaluation** — manual relevance judgment is subjective; NLP provides reproducible scores
                                                     - - **No early warning system** — search quality degrades gradually; this tool detects it before user complaints spike
                                                      
                                                       - ### 🧩 Key Product Decisions Made
                                                      
                                                       - **Two scoring modes (lexical + semantic):** Lexical (TF-IDF) works for keyword matching and is transparent. Semantic (embeddings) handles paraphrases but requires more compute. PMs choose based on their search stack maturity.
                                                      
                                                       - **NDCG as the primary metric (not just "relevance"):** Position matters — a relevant result at rank 5 is less valuable than at rank 1. NDCG captures this; simple accuracy metrics don't.
                                                      
                                                       - **Query intent classification:** Navigational, informational, and transactional queries need different evaluation criteria. A navigational query succeeds if result 1 is the right page; an informational query needs comprehensive coverage. Mixing them in one metric obscures real quality.
                                                      
                                                       - **PM recommendation generation (not just scores):** Raw NDCG numbers aren't actionable. The tool translates metric gaps into "here's what's breaking and why" — the actual output a PM needs.
                                                      
                                                       - ### 🗺 Future Roadmap
                                                      
                                                       - | Priority | Feature | Expected Impact |
                                                       - |---|---|---|
                                                       - | P0 | Live search API connection (Elasticsearch, Algolia) | Test against production search in real-time |
                                                       - | P0 | Before/after comparison mode | Measure NDCG delta between ranking model versions |
                                                       - | P1 | Human relevance labeling workflow | Crowdsource ground truth relevance labels |
                                                       - | P1 | Query clustering — group similar queries for pattern analysis | Detect query type regressions at scale |
                                                       - | P2 | Personalization signal analysis | Measure if personalized ranking improves relevance |
                                                       - | P2 | Zero-result query detection + analysis | Flag queries returning no results — often highest-value gaps |
                                                       - | P3 | Weekly search quality report (automated) | Proactive PM monitoring of search health |
                                                      
                                                       - ---

                                                       ## 📁 Project Structure

                                                       ```
                                                       ai-search-relevance-tester/
                                                       ├── app.py              # Main Streamlit dashboard
                                                       ├── scorer.py           # Relevance scoring engine (TF-IDF + embeddings)
                                                       ├── metrics.py          # NDCG, MRR, Precision@K calculation
                                                       ├── classifier.py       # Query intent classifier
                                                       ├── sample_data.py      # Sample query-result dataset
                                                       ├── requirements.txt    # Python dependencies
                                                       └── README.md           # This file
                                                       ```

                                                       ---

                                                       ## 🔗 Related Projects in This Portfolio
                                                       - [AI User Interview Analyzer](https://github.com/Poojaahegde/ai-user-interview-analyzer) — NLP theme extraction from user research
                                                       - - [FeedbackSense](https://github.com/Poojaahegde/FeedbackSense-AI-Product-Feedback-Analyzer) — User feedback clustering and sentiment
                                                         - - [A/B Test Analyzer](https://github.com/Poojaahegde/ab-test-analyzer) — Statistical significance for PM experiments
                                                          
                                                           - ---

                                                           *Built as part of an AI PM portfolio — demonstrating that search quality evaluation requires both NLP expertise and PM judgment about which metrics drive real user outcomes.*
