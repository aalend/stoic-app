from app import create_app

# Init app
app = create_app()

# Run server
if __name__ == '__main__':
    app.run(debug=True)
