from eskmo import api

api.logger.show = True

@api.start
def main():
    print(api.testing())
    api.exit()

if __name__ == "__main__":
    main()
