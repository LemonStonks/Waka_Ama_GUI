class scoring_c:
    @staticmethod
    def return_scores(data, points_reference=None):
        """
        Calculate scores based on input data.
        
        This method can handle two scenarios:
        1. Calculating scores for a single event (when points_reference is provided)
        2. Aggregating scores from multiple events (when points_reference is None)
        """
        if points_reference is not None:
            # This is for calculating scores for a single event
            # Implement your scoring logic here
            # For now, returning an empty dictionary as a placeholder
            return {}
        else:
            # This is for aggregating scores from multiple events
            # Assuming data is a list of dictionaries, each representing scores from an event
            total_scores = {}
            for event_scores in data:
                for team, score in event_scores.items():
                    if team in total_scores:
                        total_scores[team] += score
                    else:
                        total_scores[team] = score
            return total_scores

    @staticmethod
    def score_sort(scores):
        """Sort the scores in descending order."""
        return sorted(scores.items(), key=lambda x: x[1], reverse=True)