import os


def launch_analysis(data_file):
    directory = os.path.dirname(os.path.dirname(__file__))
    file = os.path.join(directory, "data", data_file)
    try:
        with open(file, 'r') as f:
            preview = f.readline()
            print("Yeah! We managed to read the file. here is a preview: {}".format(preview))
    except FileNotFoundError as e:
        print("Ow :( The file was not found. Here is the original message of the exception :", e)
    except:
        print('Destination unknown')


if __name__ == '__main__':
    launch_analysis("SyceronBrut.xml")
