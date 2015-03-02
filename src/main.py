import sys
import logger
import wikiparser

if __name__ == "__main__":
    logger.clear()
    barackPage = wikiparser.page("Barack Obama")
    logger.log(barackPage.content)
    print("See log file for result")
