"""
SearchMetrics: Computes NDCG, MRR, and Precision@K for search evaluation.
Industry-standard information retrieval metrics.
"""

import numpy as np


class SearchMetrics:
      def __init__(self, k: int = 5):
                self.k = k

      def ndcg(self, relevance_labels: list, scores: list = None) -> float:
                """
                        Normalized Discounted Cumulative Gain @ K.
                                relevance_labels: list of relevance grades (0=not relevant, 1=partial, 2=relevant, 3=highly relevant)
                                        scores: optional predicted scores for re-ranking; if None, uses labels as-is
                                                """
                labels = relevance_labels[:self.k]
                if not labels:
                              return 0.0

                dcg = sum(
                    (2 ** rel - 1) / np.log2(i + 2)
                    for i, rel in enumerate(labels)
                )

          # Ideal DCG: sort labels in descending order
                ideal_labels = sorted(labels, reverse=True)
                idcg = sum(
                    (2 ** rel - 1) / np.log2(i + 2)
                    for i, rel in enumerate(ideal_labels)
                )

          return dcg / idcg if idcg > 0 else 0.0

    def mrr(self, relevance_labels: list) -> float:
              """
                      Mean Reciprocal Rank.
                              Returns 1/rank of first relevant result (label >= 2).
                                      """
              for i, label in enumerate(relevance_labels[:self.k]):
                            if label >= 2:
                                              return 1.0 / (i + 1)
                                      return 0.0

    def precision_at_k(self, relevance_labels: list, threshold: int = 2) -> float:
              """
                      Precision@K: fraction of top-K results that are relevant.
                              """
              labels = relevance_labels[:self.k]
              relevant = sum(1 for l in labels if l >= threshold)
              return relevant / len(labels) if labels else 0.0

    def precision_at_1(self, relevance_labels: list) -> int:
              """Binary: is position 1 result relevant?"""
              return 1 if relevance_labels and relevance_labels[0] >= 2 else 0

    def coverage(self, relevance_labels: list) -> int:
              """Binary: does at least one relevant result appear in top K?"""
              return 1 if any(l >= 2 for l in relevance_labels[:self.k]) else 0
