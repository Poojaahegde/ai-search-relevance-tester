"""
QueryClassifier: Classifies search queries by intent.
Types: Navigational, Informational, Transactional
"""


NAVIGATIONAL_SIGNALS = ["settings", "dashboard", "profile", "billing", "account", "login", "admin", "home", "page", "portal"]
TRANSACTIONAL_SIGNALS = ["export", "download", "import", "create", "add", "delete", "remove", "install", "upgrade", "buy", "purchase", "cancel", "submit", "upload"]
INFORMATIONAL_SIGNALS = ["how", "what", "why", "when", "where", "difference", "guide", "tutorial", "help", "learn", "explain", "overview", "introduction"]


class QueryClassifier:
      def classify(self, query: str) -> str:
                """
                        Classify query intent based on keyword signals.
                                Returns: 'Navigational', 'Transactional', or 'Informational'
                                        """
                query_lower = query.lower()
                words = query_lower.split()

          nav_score = sum(1 for s in NAVIGATIONAL_SIGNALS if s in query_lower)
        trans_score = sum(1 for s in TRANSACTIONAL_SIGNALS if s in query_lower)
        info_score = sum(1 for s in INFORMATIONAL_SIGNALS if s in words[:3])  # Weight first words

        # Transactional queries often start with action verbs
        if words and words[0] in TRANSACTIONAL_SIGNALS:
                      trans_score += 2

        # Informational queries often start with question words
        if words and words[0] in ["how", "what", "why", "when", "where", "which", "can", "does", "is"]:
                      info_score += 2

        scores = {"Navigational": nav_score, "Transactional": trans_score, "Informational": info_score}
        return max(scores, key=scores.get) if max(scores.values()) > 0 else "Informational"
