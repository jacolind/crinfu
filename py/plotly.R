# plotly exists for python and R.
# 
# https://plot.ly/
# 
# in this script i try it out.
# 
# todo read on their website and play around here and in R.
# 
# ------------------------------------------------------------------------------

library(plotly)
p <- plot_ly(midwest, x = ~percollege, color = ~state, type = "box")
p

##

Sys.setenv("plotly_username"="jacolind")
Sys.setenv("plotly_api_key"="bw6t7eexi2")

##

packageVersion('plotly')

##

x <- c(1:100)
random_y <- rnorm(100, mean = 0)
data <- data.frame(x, random_y)
p <- plot_ly(data, x = ~x, y = ~random_y, type = 'scatter', mode = 'lines')
p


## 

trace_0 <- rnorm(100, mean = 5)
trace_1 <- rnorm(100, mean = 0)
trace_2 <- rnorm(100, mean = -5)
x <- c(1:100)

data <- data.frame(x, trace_0, trace_1, trace_2)

plot_ly(data, x = ~x, 
             y = ~trace_0, name = 'trace 0', 
             type = 'scatter', mode = 'lines') %>%
  add_trace(y = ~trace_1, name = 'trace 1', mode = 'lines+markers') %>%
  add_trace(y = ~trace_2, name = 'trace 2', mode = 'markers')

## connecting graphs 

x <- c(1:15)
y <- c(10, 20, NA, 15, 10, 5, 15, NA, 20, 10, 10, 15, 25, 20, 10)
data <- data.frame(x, y)
p <- plot_ly(data, x = ~x, y = ~y, name = "Gaps", 
             type = 'scatter', mode = 'lines') %>%
  add_trace(y = ~y - 5, name = "<b>No</b> Gaps", connectgaps = TRUE)
p

## annotate 

annotation_1 <- list(x = 2, y = data[data$x == 2, "y"],
                     showarrow = FALSE, xanchor = 'left',
                     text = "look here!", 
                     font = list(size = 12, color = 'red')
                     )

color_gray <-  'rgb(204, 204, 204)'
font <- list(family = 'Arial',
             size = 12,
             color = color_gray)


yaxis <- list(title = "",
              showgrid = FALSE,
              zeroline = FALSE,
              showline = TRUE,
              showticklabels = TRUE,
              linecolor = color_gray,
              linewidth = 2,
              ticks = 'outside',
              tickcolor = color_gray
              )

xaxis <- list(title = "",
              showline = TRUE,
              showgrid = FALSE,
              showticklabels = TRUE,
              linecolor = color_gray,
              linewidth = 2,
              ticks = 'outside',
              tickcolor = color_gray,
              tickwidth = 2,
              autotick = FALSE,
              ticklen = 5
              )

p %>%
  layout(showlegend = FALSE, title = "Connecting lines") %>%
  layout(annotations = annotation_1) %>%
  layout(xaxis = xaxis, yaxis = yaxis)


## stats 

month <- c('January', 'February', 'March', 'April', 'May', 'June', 'July',
           'August', 'September', 'October', 'November', 'December')
high_2014 <- c(28.8, 28.5, 37.0, 56.8, 69.7, 79.7, 78.5, 77.8, 74.1, 62.6, 45.3, 39.9)
low_2014 <- c(12.7, 14.3, 18.6, 35.5, 49.9, 58.0, 60.0, 58.6, 51.7, 45.2, 32.2, 29.1)
data <- data.frame(month, high_2014, low_2014)
data$average_2014 <- rowMeans(data[,c("high_2014", "low_2014")])

#The default order will be alphabetized unless specified as below:
data$month <- factor(data$month, levels = data[["month"]])

xaxis <- list(title = "Months",
              gridcolor = 'rgb(255,255,255)',
              showgrid = TRUE,
              showline = FALSE,
              showticklabels = TRUE,
              tickcolor = 'rgb(127,127,127)',
              ticks = 'outside',
              zeroline = FALSE)
yaxis <- list(title = "Temperature (degrees F)",
              gridcolor = 'rgb(255,255,255)',
              showgrid = TRUE,
              showline = FALSE,
              showticklabels = TRUE,
              tickcolor = 'rgb(127,127,127)',
              ticks = 'outside',
              zeroline = FALSE)

p <- plot_ly(data, x = ~month, y = ~high_2014, type = 'scatter', mode = 'lines',
             line = list(color = 'transparent'),
             showlegend = FALSE, name = 'High 2014') %>%
  add_trace(y = ~low_2014, type = 'scatter', mode = 'lines',
            fill = 'tonexty', fillcolor='rgba(0,100,80,0.2)', 
            line = list(color = 'transparent'),
            showlegend = FALSE, name = 'Low 2014') %>%
  add_trace(x = ~month, y = ~average_2014, type = 'scatter', mode = 'lines',
            line = list(color='rgb(0,100,80)'),
            name = 'Average') %>%
  layout(title = "Average, High and Low Temperatures in New York",
         paper_bgcolor='rgb(255,255,255)', plot_bgcolor='rgb(229,229,229)',
         xaxis = xaxis,
         yaxis = yaxis)
p

## convert ggplot object to plotly 

# todo read url and make it 

# https://plot.ly/ggplot2/user-guide/#modify-ggplot2-figure
dsamp <- diamonds[sample(nrow(diamonds), 1000), ]
q <- qplot(carat, price, data=dsamp, colour=clarity)
gp <- ggplotly(q)
gp

gp %>%
  layout(dragmode = "pan")

# As mentioned previously, ggplotly() translates each ggplot2 layer into one or more plotly.js traces. In this translation, it is forced to make a number of assumptions about trace attribute values that may or may not be appropriate for the use case. The style() function is useful in this scenario, as it provides a way to modify trace attribute values in a plotly object. Furthermore, you can use the plotly_build() function.


?plotly_build

# https://rdrr.io/cran/plotly/man/ggplotly.html






## shiny and plotlyt and ggplot

library(shiny)
library(ggplot2)
library(ggthemes)
library(plotly)

ui <- fluidPage(
  titlePanel("Plotly"),
  sidebarLayout(
    sidebarPanel(),
    mainPanel(
      plotlyOutput("plot2"))))

server <- function(input, output) {
  
  output$plot2 <- renderPlotly({
    print(
      ggplotly(
        ggplot(data = mtcars, aes(x = disp, y = cyl)) + 
          geom_smooth(method = lm, formula = y~x) + 
          geom_point() + 
          theme_gdocs())
    )
    
  })
}

shinyApp(ui, server)

# todo keep on tweaking that example 



# another shiny example 
ui <- fluidPage(
  plotlyOutput("plot"),
  verbatimTextOutput("event")
)

server <- function(input, output) {
  
  # renderPlotly() also understands ggplot2 objects!
  output$plot <- renderPlotly({
    plot_ly(mtcars, x = ~mpg, y = ~wt)
  })
  
  output$event <- renderPrint({
    d <- event_data("plotly_hover")
    if (is.null(d)) "Hover on a point!" else d
  })
}

shinyApp(ui, server)

## todo read ref https://plot.ly/r/reference/#scatter

## see color by numerical variable: aes(color = ~carat) 

d <- diamonds[sample(nrow(diamonds), 1000), ]
plot_ly(d, x = ~carat, y = ~price,
        # Hover text:
        text = ~paste("Price: ", price, '$<br>Cut:', cut),
        color = ~carat, size = ~carat)

## hovermode: compare vs closest

p <- plot_ly(data = iris, x = ~Sepal.Length, y = ~Petal.Length, color = ~Species)

p %>%
  layout(hovermode = 'compare')

p %>%
  layout(hovermode = 'closest')


## scatter w marker 

marker <- list(size = 10,
               color = 'rgba(255, 182, 193, .9)',
               line = list(color = 'rgba(152, 0, 0, .8)',
                           width = 2))

plot_ly(data = iris, x = ~Sepal.Length, y = ~Petal.Length,
        marker = marker) %>%
  layout(title = 'Styled Scatter',
         yaxis = list(zeroline = FALSE),
         xaxis = list(zeroline = FALSE))

## todo next. read cheat sheet and continue with tutorial: histogram etc, see tabs.

## dropdown menu 

library(MASS)

covmat <- matrix(c(0.8, 0.4, 0.3, 0.8), nrow = 2, byrow = T)
df <- mvrnorm(n = 10000, c(0,0), Sigma = covmat)
df <- as.data.frame(df)

colnames(df) <- c("x", "y")
p <- plot_ly(df, x = ~x, y = ~y, alpha = 0.3) %>%
  add_markers(marker = list(line = list(color = "black", width = 1))) %>%
  layout(
    title = "Drop down menus - Plot type",
    xaxis = list(domain = c(0.1, 1)),
    yaxis = list(title = "y"),
    updatemenus = list(
      list(
        y = 0.8,
        buttons = list(
          
          list(method = "restyle",
               args = list("type", "scatter"),
               label = "Scatter"),
          
          list(method = "restyle",
               args = list("type", "histogram2d"),
               label = "2D Histogram")))
    ))
p


## dropdown menu two 

x <- seq(-2 * pi, 2 * pi, length.out = 1000)
df <- data.frame(x, y1 = sin(x), y2 = cos(x))

p <- plot_ly(df, x = ~x) %>%
  add_lines(y = ~y1, name = "A") %>%
  add_lines(y = ~y2, name = "B", visible = F) %>%
  layout(
    title = "Drop down menus - Styling",
    xaxis = list(domain = c(0.1, 1)),
    yaxis = list(title = "y"),
    updatemenus = list(
      list(
        y = 0.8,
        buttons = list(
          
          list(method = "restyle",
               args = list("line.color", "blue"),
               label = "Blue"),
          
          list(method = "restyle",
               args = list("line.color", "red"),
               label = "Red"))),
      
      list(
        y = 0.7,
        buttons = list(
          list(method = "restyle",
               args = list("visible", list(TRUE, FALSE)),
               label = "Sin"),
          
          list(method = "restyle",
               args = list("visible", list(FALSE, TRUE)),
               label = "Cos")))
    )
  )
p

## financial plot w range slider 

# https://plot.ly/r/range-slider/
library(quantmod)

# Download some data
getSymbols(Symbols = c("AAPL", "MSFT"))

ds <- data.frame(Date = index(AAPL), AAPL[,6], MSFT[,6])

p <- plot_ly(ds, x = ~Date) %>%
  add_lines(y = ~AAPL.Adjusted, name = "Apple") %>%
  add_lines(y = ~MSFT.Adjusted, name = "Microsoft") %>%
  layout(
    title = "Stock Prices",
    xaxis = list(
      rangeselector = list(
        buttons = list(
          list(
            count = 3,
            label = "3 mo",
            step = "month",
            stepmode = "backward"),
          list(
            count = 6,
            label = "6 mo",
            step = "month",
            stepmode = "backward"),
          list(
            count = 1,
            label = "1 yr",
            step = "year",
            stepmode = "backward"),
          list(
            count = 1,
            label = "YTD",
            step = "year",
            stepmode = "todate"),
          list(step = "all"))),
      
      rangeslider = list(type = "date")),
    
    yaxis = list(title = "Price"))


## anmimation 

df <- data.frame(
  x = c(1,2,1), 
  y = c(1,2,1), 
  f = c(1,2,3)
)

df %>%
  plot_ly(
    x = ~x,
    y = ~y,
    frame = ~f,
    type = 'scatter',
    mode = 'markers',
    showlegend = F
  )

library(gapminder)


p <- gapminder %>%
  plot_ly(
    x = ~gdpPercap, 
    y = ~lifeExp, 
    size = ~pop, 
    color = ~continent, 
    frame = ~year, 
    text = ~country, 
    hoverinfo = "text",
    type = 'scatter',
    mode = 'markers'
  ) %>%
  layout(
    xaxis = list(
      type = "log"
    )
  )
p

# todo i do not get the same output as these examples. or it cannot be played in the RSTudio editor?

# todo try to do an animation with corr matrix over time 

# for more see https://plot.ly/r/


