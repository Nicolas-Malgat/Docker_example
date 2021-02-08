from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
   return """
        <img class="fit-picture"
     src="https://miro.medium.com/max/680/1*NXZYK4_f0lFJ8gpgcE5tHA.png"
     alt="Grapefruit slice atop a pile of other slices">
   """
   
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")