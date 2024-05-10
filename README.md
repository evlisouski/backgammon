### test task for the position of python backend developer
# Service for backgammon game score calculation

The service performs calculation of the game score and determines the type of victory depending on the final arrangement of checkers on the playing field on the opponent's side.

# <a id="Content"></a> Content:
 
 - [Definitions](#definitions)
 - [Project structure](#projectstructure)
 - [Tests](#tests)
 - [Docker](#docker)

# <a id="definitions"></a> Definitions
- `home board` - playing field area from 1 to 6 points.
- `outer board` - playing field area from 7 to 12 points.
- `opponent outer board` - playing field area from 13 to 18 points.
- `opponent home` - playing field area from 19 to 24 points.
- `bar` - every checker that is hit is sent to the bar which is a holding zone for all checkers before reentering into a home board.
- `koks` - a situation in which the defeated player was unable to remove one or more of his checkers from the winners home or left a checker on the bar, while the winner brought all his checkers off the board.
- `mars` - the position of the checkers at the end of the game in which the defeated player did not have time to bring all his checkers into his house, while the winner brought everything out of the board. Such a victory brings 2 points.
- `oin` - the position of checkers at the end of the game, in which the defeated player has had time to discard at least 1 checker, while the winner has taken all of them off the board. Counts as 1 point.

<div align="center">
    <image src="./docs/Backgammon_(checker placement on the opponent's side).png">
    <p> Fig. 1 - numbering of the playing field from the opponent's side</p>
</div>



# <a id="projectstructure"></a> Project structure
- `src` - directory containing project files.
- - `score` - directory containing the files necessary for calculating the game score and the related endpoints.
- - `tests` - directory with files tests.
- - `main.py` - main file to run the application.
- `requirements.txt` - file with dependencies for pip manager.




# <a id="restapi"></a> API

Interactive API documentation (OpenAPI format,) and web user interfaces are available by default at http://127.0.0.1:8000/docs
<div align="center">
    <image src="./docs/FastAPI_endpoints.png">
    <p> Fig. 2 - Interactive API documentation</p>
</div>

## Calculate score
To calculate the number of points and the winner's victory type, you need to execute a POST request according to the provided scheme `SGameResultInput` for endpoint `/score/calculate_score`.
<p>! Warning</p>
It is necessary to note that for the calculation the numbering of points is done from the opponent's side (fig. 1) and it is necessary to send the final position of the checkers to JSON from the opponent's side. For example, koks will be if at least one checker is at point 19-24.


# <a id="tests"></a>Tests 
The tests are written using pytest. To run the tests, run the `pytest` command in the project root directory in the `bash`. The `conftest.py` file is responsible for configuring the tests, in particular the client for intergation tests. The tests themselves, unit tests and intergation tests, are located in the `src\tests`.

# <a id="docker"></a>Docker 
To run the application in a docker container, run the `docker compose up` command while in the root of the project. By default, the application port will be forwarded to host port `8000`. After launching, you can view the application's online documentation at http://127.0.0.1:8000/docs.