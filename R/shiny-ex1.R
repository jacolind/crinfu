# similar to https://shiny.rstudio.com/tutorial/written-tutorial/lesson6/

ui <- fluidPage(
  selectInput("assets",
              label = "type in all names you want. autocomplete ON",
              choices = unique(df$symbol),
              multiple = TRUE, selectize = TRUE
  ),
  dateRangeInput("dates", "choose date range.",
                 start = "2015-04-01",
                 end = "2018-01-01",
                 # allowed range. 
                 # tood use min(df$date) instead
                 min =  "2014-01-01",  
                 max = "2018-06-06" 
  ),
  actionButton("done", "click to show result"),
  # output 
  plotOutput("plot"),
  tableOutput("tbl")
)

# server 
server <- function(input, output){
  # df_3 <- df %>%
  #     filter(symbol %in% input$assets) %>%
  #     select(symbol, mcap) %>%
  #     head()
  data <- reactive({
    df_plot <- df %>%
      filter(symbol %in% input$assets) %>%
      filter(date > input$dates[1], 
             date < input$dates[2]) %>%
      select(date, symbol, mcap)
    })
  output$tbl <- renderTable(
    data() %>% 
    group_by(symbol) %>%
    summarise(mean(mcap)/10^9))
  output$plot <- renderPlot(
    ggplot(data(), aes(x=date, y=mcap, color=symbol)) + 
      geom_line()
  )
}

shinyApp(ui, server)
