# Provisional COVID-19 infrastructure induces large, rapid increases in cycling
## Things looked up
**Status-Quo bias** -> People wont change soemthing in their life that already works; the percieved cost and effort of switching baises them to reamin the same.
**Default-Effects** -> People are more likely to remain with a defualt option since it takes effort and thinking to switch.
**Time-inconsistent preferances** -> People are disconnected form their future selves so they ingnore options that will help in the long run.
**Shovel-ready** -> A construction project is ready to begin construction; no more planning is needed.
**Panel Data** -> Type of data where the same *individuums* are recorded at different periods in time. This focuses on the effect on individuals rather than the effect on average.
**Endogeneity** -> Estimator is biased/*inconsistent* because of Omitted variables, measurement error or reverse causality.
**Panel Regression** -> Method of regression that uses panel data 

## Notes for first draft
1. **Aims and Stated Contributions**
	Aim -> To find the effect of increased bike infrastructure on number of people biking
	Contribution -> Data on large amouts of bike lanes being added quickly
	Contribution -> How we can switch peoples habbits quickly
	Contribution -> Effect of bike lanes one large roads
	
2. **Methods for Collecting and Processing data**
	Collecting -> Scraping
	Collecting -> Cities split into treated and contorll based on treatment after the fact
	Collecting -> Talking with policymakers for sceduling converns
	Collecting -> Period of effect (days before vs days affter)
	Processing -> Fixxed Effect panel regression (city week)
	Processing -> City fixxed effects from counters in the same city
	Processing -> Differance in differances, log of bicicle counts
	Collecting -> Routing Searches apple maps
	Collecting -> Total percipitation, mean wind, temperature and sunshine
3. **Statistical Methods used and how applied to data**
	Method -> Fixxed Effect panel regression
	Method -> Differance in diferances
	Method -> comparing regressions
	
4. **Data -> Conclusion**
	Conclusion -> "Robust evidence for substantial short-run increases in cycling in European cities due to new provisional cycling infrastructure" <- Good, many controls, shows over many permutations, prefered specification has largest confidence interval
	Good controls for many outcomes with fixxed effects
	Intercity fixxed effects from bike counters so good contorls for city differences (design of study counter level study)
	Good comparison of measures of treatment (Binary, Length, Length per capita and length per km^2 -> comparison to other measurments shows its not cuased by anouncments as if it was the effect wouldn't show
	Controls for city density -> km vs km per sqkm
	Apple maps -> contorls for increase in bike being cause by factors reducing availability of transport from construction
	Subnational changes contorlled for <- facebook data
	Shows that in covid many people who are traveling are biking but there could be selection where people who would bike are the ones who would go out anyways (facebook data)
	
5. **Limitations**
	During covid
	Cities used
	Non-random -> Green preferances and information about COVID  (controled by having other cities with similar COVID rhetoric) relating to biking could explain effect partially -> Assumed control cities and treated cities would evolve on similar trajectories (gree preferances) opposite due to "mobility reductions due to covid"
	Reverse causality (third varaible) -> time span (limited) only if days are random (confirmed by policymakers in 2 cities)
	Teatment at a city level
	Should measure availability of infastructure to a counter level
	Smaller sample due to controling for changes to public transport availability <- apple maps
	quality of implementation missing
	Doesn't take into account policy of public announcement effects for within the effect period
6. **Ethical Issues**
	Tracking user movements, tracking, data scraping, fudging the numbers
	