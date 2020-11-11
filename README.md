# FOOTBALL PLAYER USING CORRELATION AND RULE-BASED ANALYSIS

## Background

There are many aspects of technology that can be used to improve the game as well as to get the statistics of a football player, and these sources of data prove that there are many aspects that can be analysed from a player by using the Big Data approach.

Questions asked : Is there any skills that are related to each other or are there skills that are opposite to each other?

One approach is by analysing the correlation between two skills, and another the approach is to analyse them using association rule approach — analysing what is present and what is absent in a football player’s skill.

## Purpose

Determine the related and opposite skills in football players using correlation and Association Rule Learning

## Basic Theory

![CorrelationFormula](https://github.com/tefohulu/footballplayeranalysis/blob/main/Correlation.png)

![MBAFormula](https://github.com/tefohulu/footballplayeranalysis/blob/main/Frequency.png)

## Diagram Process

![DiagramProcess](https://github.com/tefohulu/footballplayeranalysis/blob/main/Diagram%20Process.png)

## Results

![PositiveOutfieldCorrelation](https://github.com/tefohulu/footballplayeranalysis/blob/main/%2BCO.png)

![NegativeOutfieldCorrelation](https://github.com/tefohulu/footballplayeranalysis/blob/main/-CO.png)

![PositiveGoalkeeperCorrelation](https://github.com/tefohulu/footballplayeranalysis/blob/main/%2BCG.png)

![NegativeGoalkeeperCorrelation](https://github.com/tefohulu/footballplayeranalysis/blob/main/-CG.png)

![PositiveOutfieldRules](https://github.com/tefohulu/footballplayeranalysis/blob/main/%2BRO.png)

![NegativeOutfieldRules](https://github.com/tefohulu/footballplayeranalysis/blob/main/-RO.png)

![PositiveGoalkeeperRules](https://github.com/tefohulu/footballplayeranalysis/blob/main/%2BRG.png)

![NegativeGoalkeeperRules](https://github.com/tefohulu/footballplayeranalysis/blob/main/-RG.png)


## Conclusion

* While the correlation analysis also considers the tendency of the data, the rules only considers the occurrence of the data

* Rule analysis giving a different approach on a negative correlation analysis, where one aspect of the rule must be reduced from the default positive correlation to get the desired results

* Both correlation analysis and rules analysis giving a total of 8 set of attribute relation. The threshold of correlation analysis is given so that every set of rules give a limited set of rules, while the rules analysis is taken from top 95% percentile of the order of the rules on both sides.

* The total of relations based on correlation analysis given on outfield players are 9 for strong positive and 10 for strong negative. For the goalkeepers, there are 10 strong positive and 6 strong negative. The total of relations based on rules analysis given on outfield players are 6 for strong positive and 10 for strong negative. For the goalkeepers, there are 1 strong positive and 3 strong negative.

* The attributes are distributed quite equally on both correlation and rules analysis, showing that there is no strongest skill that is dominant enough on the dataset. However, this did not apply on strong negative correlations on goalkeepers using correlation approach, where temperament dominates almost all the rules.

## Suggestions

- Consider position, age, height and weight, preferred skills, or price to get a better understanding of a player. 

- It can be done a correlation between football position and skills. 

- Analyse a set of football skills given, and determine if this player either have a defensive mentality or an offensive mentality. However, some leagues/countries skills are quite low compared to others, there will be a bias on determining the skills.  

- Expand with more set of data.

- These analyses of football player skills can be used to build an expert-based system, where it can be determined the player who is the closest to a player, or a player who can be an anti to another player. 
