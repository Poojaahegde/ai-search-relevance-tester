"""
RelevanceScorer: Scores query-result relevance using TF-IDF cosine similarity.
Optional semantic mode using sentence-transformers (if installed).
"""

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class RelevanceScorer:
      def __init__(self, mode: str = "tfidf"):
                self.mode = mode
                self.model = None

          if mode == "semantic":
                        try:
                                          from sentence_transformers import SentenceTransformer
                                          self.model = SentenceTransformer("all-MiniLM-L6-v2")
except ImportError:
                print("sentence-transformers not installed. Falling back to TF-IDF.")
                self.mode = "tfidf"

    def score(self, query: str, results: list) -> list:
              """
                      Score relevance of each result for the given query.
                              Results: list of dicts with 'result_title' and 'result_content'.
                                      Returns: list of relevance scores (0.0 to 1.0), one per result.
                                              """
              result_texts = [
                  f"{r.get('result_title', '')} {r.get('result_content', '')}"
                  for r in results
              ]

        if not result_texts:
                      return []

        if self.mode == "semantic" and self.model:
                      return self._semantic_score(query, result_texts)
else:
            return self._tfidf_score(query, result_texts)

    def _tfidf_score(self, query: str, result_texts: list) -> list:
              """TF-IDF cosine similarity scoring."""
              corpus = [query] + result_texts
              vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
              try:
                            tfidf_matrix = vectorizer.fit_transform(corpus)
                            query_vec = tfidf_matrix[0]
                            result_vecs = tfidf_matrix[1:]
                            scores = cosine_similarity(query_vec, result_vecs)[0]
                            return scores.tolist()
except Exception:
            return [0.0] * len(result_texts)

    def _semantic_score(self, query: str, result_texts: list) -> list:
              """Sentence-BERT semantic similarity scoring."""
              try:
                            query_embedding = self.model.encode([query])
                            result_embeddings = self.model.encode(result_texts)
                            scores = cosine_similarity(query_embedding, result_embeddings)[0]
                            return scores.tolist()
except Exception:
            return self._tfidf_score(query, result_texts)
