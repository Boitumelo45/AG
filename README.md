# BPAG

```
    Author      : Boitumelo Phetla
    DATE        : 4/10/2021 18:18
    Description : project outline and structure
```

## Assumptions

```assumptions

1. under user.txt
    assumption: All users are unique and follows the same string format <str>.title()
2. under tweet.txt
    assumption: All tweets are chronological

If user follows someone and user has no tweets then log tweets from 
users the user is following

e.g.
    Martin: has no tweets, but follows Alan
    
    output >>>
    
    Martin
            @Alan: If you have a procedure with 10 parameters, you probably missed some.
            @Alan: Random numbers should not be generated with a method chosen at random.

in user.txt
    if a user follows a list of names without commas the names are assumped as one
    e.g.
        Martin follows Alan Ward James Cody
        this is read as 
        Martin -> (Alan Ward James Cody) as a single name 

if user.txt is empty throw Exception

Alan follows Martin, Ward
comma(,) is designated as a delimiter, assumption is [-, .] are used in as name extensions like
    e.g. Dave K. Malan, or Dave-Karl Malan are valid names
```
## How to use code

```commandline
    code structure:
        AG/
        └───app
        ├───controller
        │   ├───data
    
    1. How to run application
    cd AG
    $ python -m app
    
    output:
    Alan
            @Alan: If you have a procedure with 10 parameters, you probably missed some.
            @Alan: Random numbers should not be generated with a method chosen at random.
    Martin
    Ward
            @Alan: If you have a procedure with 10 parameters, you probably missed some.
            @Ward: There are only two hard things in Computer Science: cache invalidation, naming things and off-by-1 errors.
            @Alan: Random numbers should not be generated with a method chosen at random.

    2. How to run unittest
    cd AG
    $ python -m unittest
    
    output:
    ----------------------------------------------------------------------
    Ran 11 tests in 0.002s
    
    OK
```

### Code structure
```debugging
    AG/
        app/
            controller/
                data/
                    requirements.txt
                    tweet.txt
                    user.txt
                __init__.py
                test_tweet.py
                test_user.py
                user.py
                tweet.py
            __init__.py
            __main__.py
            setup.py
        README.md
```