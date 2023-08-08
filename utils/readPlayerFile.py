def read_player_file(url):
    try:
        with open(url, "r") as file:
            lines = file.readlines()
            
            data =  [line.split(',')[1] for line in lines]
            return data
    except FileNotFoundError:
        print("File not found.")
        data = []
        return data