from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()

def empty_func():
    return "tunahan"

@app.get("/{echo_str}")
async def read_main(echo_str: str):
    return {"echo": echo_str}



@app.get("/", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
    
    
    <body style="background-color: black;">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Rampart+One&display=swap" rel="stylesheet"> 
    <div id="text" style="font-size: 100;color: red;height: 100%; display: flex; justify-content: center; align-items: center; font-family: 'Rampart One', cursive;">
            <div style="display: flex; flex-direction: row;">
                <div id="l1">
                    Merhaba
                </div>
                <div id="l2">
                    ,&nbsp;
                </div>
                <div id="l3">
                    Dünya
                </div>
                
            </div>
            <div>
                <img src="http://i.stack.imgur.com/SBv4T.gif" alt="this slowpoke moves"  width="250" />
            </div>
        </div>

        <script>
                function getColor() {
                    var letters = '0123456789ABCDEF';
                    var color = '#';
                    for (var i = 0; i < 6; i++) {
                    color += letters[Math.floor(Math.random() * 16)];
                    }
                    return color
                }
                setInterval(() => {
                    document.getElementById("l1").style.color = getColor();
                    document.getElementById("l2").style.color = getColor();
                    document.getElementById("l3").style.color = getColor();
                    
                },300)
        </script>
    </body>
        
    </html>
    """
    
