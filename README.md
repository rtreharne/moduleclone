# AutoModerator

This tool will:

+ Get submissions for a single assignment on Canvas
+ Identify issues for moderation
+ Save the report as an .xlsx file

The following rules are used to flag issues for moderation.

1. Feedback Word Count: Any submission that has a feedback comment word count less than the mean word count for all submissions are flagged.
2. Rubric/Score Discrepancies: Any submission for which there is a difference between the totalled rubric score and final awarded score.
3. Marker Mean Scores: Any submissions belonging to a marker that has awarded an average score that is below or above one standard devation from the mean score (for the assignment)
4. Marker Score Variation: Any submissions belonging to a marker that has an average standard devation that is below one standard deviation from the mean standard devation (for the assignment)


