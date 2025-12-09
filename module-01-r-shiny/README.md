# Module 01: R and Shiny

## Learning Objectives

- Understand the fundamentals of R programming for data analysis
- Learn to work with sports data using the tidyverse
- Build interactive web applications with Shiny
- Create visualizations for sports analytics

## Prerequisites

- Basic programming knowledge
- Familiarity with data analysis concepts

## Getting Started

This module uses a dev container with R and Shiny pre-installed. To get started:

1. Make sure you have Docker and VS Code with the Dev Containers extension installed
2. Open this folder in VS Code
3. When prompted, click "Reopen in Container"
4. Wait for the container to build and install dependencies

## Contents

- `app.R`: Starter Shiny application template
- `data/`: Sample sports data files
- `exercises/`: Practice exercises
- `assignments/`: Module assignments

## Running Your Shiny App

Once in the dev container, you can run your Shiny app with:

```r
shiny::runApp('app.R', host='0.0.0.0', port=3838)
```

The app will be accessible at http://localhost:3838

## Resources

- [R for Data Science](https://r4ds.had.co.nz/)
- [Shiny Documentation](https://shiny.rstudio.com/)
- [tidyverse](https://www.tidyverse.org/)
