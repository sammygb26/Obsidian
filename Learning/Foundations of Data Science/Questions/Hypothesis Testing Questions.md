What is the method of hypothesis testing? #flashcard #FDS #HypothesisTesting
	We take something we want to test if it could be true. So we assume it is false and call this the null hypothesis. We describe that with a statistical model of a statistic which matters based on our hypothesis. We then compare this model to a test statistic we have calculated form real data. If our test statistic is either in a rejection region or we have a p value suggesting statistical significance we can see our collected is to a level incompatible with our null hypothesis. This may suggest the null hypothesis could be false hence our alternative hypothesis could be correct. 

---
What are rejection regions? #flashcard #FDS #HypothesisTesting
	Rejection regions is a way of deciding if we should reject the null hypothesis or not. The idea is we select a rejection probability mass and if our test statistic is beyond the critical value for the probability mass (in the left, right or both directions) we reject it.

---
What is a lower-tailed, two-tailed and higher-tailed rejection region? #flashcard #FDS #HypothesisTesting
	These are the types of region we could reject a null hypothesis based on. We determine this based on our alternative hypothesis which would be more likely if the test statistic is much lower, much higher or much more extreme as the alternative hypothesis could explain (lower-tailed, higher-tailed, two-tailed respectively).

---
What are the ways of finding rejection boundaries? #flashcard #FDS #HypothesisTesting
	We could either use a bootstrap method to find critical values or we could use a statistical model to find critical values. The critical values we would want would depend on our rejection percentage and if we had a lower, higher or two tailed rejection region.

---
What is the chi-squared statistic? #flashcard #FDS #HypothesisTesting
	This measures the difference from an expected values and actual values. It is equal to the sum of the squared differences of observed and expected values relative to the expected values.

---
How can we find the degrees of freedom for a chi-squared distribution? #flashcard #FDS #HypothesisTesting
	We find out the minimum number of varying values needed to calculate the other. This can change depending on if we have fixed totals in our example. For example if we were looking at portions of a population with a fixed size.

---
What are Type I and Type II errors in hypothesis testing and how can we reduce their likelihood? #flashcard #FDS #HypothesisTesting
	Type I -> Our null hypothesis is actually correct yet we happen to get a test statistic in the rejection region or with a p-value suggesting statistical significance. This can be reduced in likelihood by reducing the p value boundary for statistical significance or reducing rejection percentage.
	Type II -> Our null hypothesis is false yet we happen to get a test statistic that doesn't reject it anyway. We can't get around this without further investigation.

---
What are some problems with hypothesis testing? #flashcard #FDS #HypothesisTesting
	We can base policy decisions on if  test statistics pass a fixed value but just because this part of the hypothesis test is passed doesn't mean it is true and more investigation is needed.
	Data snooping and p-value hacking allow people to fake statistical significance or remove it by choosing what data to include and exclude.
	Multiple testing and a bias toward reporting statistically significant results means we can becomes tricked by Type I errors since they will happen in any population by chance.

---
What is the definition of a p-value for a statistic? #flashcard #FDS #HypothesisTesting
	The p-value for a statistic relates to a statistical model described for a null hypothesis. The p-value is the percentage mass that is more extreme than the statistic's value itself.

---
What is statistical significance? #flashcard #FDS #HypothesisTesting
	If we have some alternative hypothesis and the p-value we get from looking at the null hypothesis instead gives a p-value less than a set value (usually 0.05) we say this result is statistically significant. This weighs in favor of our alternative hypothesis.

---
