
ALLOWED_EXTENSIONS = {'jpeg', 'jpg', 'png'}

def allowed_file(filename):
    if '.' not in filename:
        return '.' in filename
    return filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


if __name__ == '__main__':
        fnm = input("give filename: ")
        if allowed_file(fnm):
            print("good")
        else:
            print("bad")
