"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?



# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?

 


# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the brand_id of ``ram``.
brand = Brand.query.get('ram')
## >>> brand
##<Brand_name: Rambler Brand_id: ram> class Brand object

# Get all models with the name ``Corvette`` and the brand_id ``che``.
models = Model.query.filter(Model.name=='Corvette', Model.brand_id=='che').all()
# >>> models (list of objects)
# [<Model: 1953 Corvette Model_id: 5, <Model: 1954 Corvette Model_id: 6, 
# <Model: 1955 Corvette Model_id: 8, <Model: 1956 Corvette Model_id: 10, 
# <Model: 1957 Corvette Model_id: 11, <Model: 1958 Corvette Model_id: 13, 
# <Model: 1959 Corvette Model_id: 17, <Model: 1960 Corvette Model_id: 20, 
# <Model: 1961 Corvette Model_id: 25, <Model: 1962 Corvette Model_id: 27, 
# <Model: 1963 Corvette Model_id: 37, <Model: 1964 Corvette Model_id: 38]

# Get all models that are older than 1960.
models = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
brands = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with ``Cor``.
q5 = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = Brand.query.filter(Brand.founded=='1903', Brand.discontinued==None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = Brand.query.filter((Brand.discontinued != None) |( Brand.founded < 1950)).all()

# Get all models whose brand_id is not ``for``.
q8 = Model.query.filter(Model.brand_id != 'for').all()



# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    models = Model.qurey.filter(Model.year==year).all()

    if models:
        for model in models:
            print(f"Brand Name: {model.brand.name}\nHeadquarters: {model.brand.headquarters}")
            


def get_brands_summary():
    """Prints out each brand name (once) and all of that brand's models,
    including their year, using only ONE database query."""

    brands = Brand.query.all()

    for brand in brands:
        print(brand.name)
        if brand.models:
            for model in brand.models:
                print(model)

def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    return Brand.query.filter(Brand.name.like('%mystr%')).all()


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    return Model.query.filter((Model.year >= start_year) & (Model.year < end_year)).all()

