FROM rstudio/plumber
ENV RENV_PATHS_LIBRARY renv/library
# RUN R -e "install.packages('plumber')"
RUN R -e "install.packages('renv', repos = c(CRAN = 'https://cloud.r-project.org'))"

COPY app-r-api /usr/src
WORKDIR /usr/src

RUN R -e "renv::restore()"

CMD ["Rscript", "/usr/src/R/rest.R"]