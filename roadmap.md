## Introduction: 

There are two libraries associated with this project so far: [a reader](https://github.com/jsfenfen/990-xml-reader) and [an admin repo](https://github.com/jsfenfen/irs990_admin). The reader distills down the logic of reading the forms; the admin is needed, however, to read the .xsd files and generate the variable reference files the reader needs, as well as to generate the sql alchemy schemas or django model files as needed. The admin will include the database entry part.


## Roadmap: 

Variable name standardization / canonicalization: 

- variable name standardization (map variables across years)

- variable name type standardization (assign least restrictive data type to a given canonical variable)

DB Schema generation / django:

- db schema generation (Create a django models file or a sql alchemy file)

- db loader step : Load data from a generic form into the db one commit at a time.

Loading / load optimization: 

- db loader 2: load data from forms in aggregate for better loading time. 

- db load 3: load should run completely. 

- Open question: sqlalchemy ? Rails ? [ we're mostly concerned with making postgres go faster ]


following weeks:

- Clean up python code so that it's releaseable.

 

- Rails templates + data side of things, representing data for nonprofit explorer etc. 
- DB side: are we serving json blobs? 


