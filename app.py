import os
from flask import Flask, render_template_string

app = Flask(__name__)

SURFBOARDS = [
    {"name": "The Longboard (Malibu)", "size": "8'0\" - 10'0\"", "shape": "High volume, rounded nose, single fin", "best_for": "Small waves, beginners, effortless gliding"},
    {"name": "The Funboard / Hybrid", "size": "6'8\" - 7'6\"", "shape": "Wider template, fuller nose", "best_for": "Progressing surfers, messy or small-to-medium surf"},
    {"name": "The Shortboard (Thruster)", "size": "5'8\" - 6'4\"", "shape": "Narrow, pointed nose, rocker curve, 3 fins", "best_for": "Fast, hollow, powerful waves and high-performance maneuvers"},
    {"name": "The Fish", "size": "5'2\" - 6'0\"", "shape": "Short, wide, swallow tail, twin fin setup", "best_for": "Small, weak summer waves where you need speed in minimal pocket"}
]

@app.route("/")
def home():
    env = os.environ.get("ENVIRONMENT", "development")
    version = os.environ.get("APP_VERSION", "v1.0.0")
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Quiver & Wave | Surfboard Guide</title>
        <style>
            body { font-family: Arial, sans-serif; background: #e0f7fa; color: #006064; margin: 0; padding: 20px; }
            .container { max-width: 800px; margin: auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
            h1 { color: #00838f; border-bottom: 2px solid #b2ebf2; padding-bottom: 10px; }
            .meta { background: #e0f2f1; padding: 10px 15px; border-radius: 5px; font-size: 0.9em; margin-bottom: 20px; }
            .board { border-bottom: 1px solid #eee; padding: 15px 0; }
            .board:last-child { border-bottom: none; }
            h3 { margin: 0 0 5px 0; color: #004d40; }
            p { margin: 5px 0; }
        .tag { display: inline-block; background: #00acc1; color: white; padding: 3px 8px; border-radius: 3px; font-size: 0.8em; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Quiver & Wave 🏄‍♂️</h1>
            <div class="meta">
                <strong>Environment:</strong> <span class="tag">{{ env }}</span> | 
                <strong>App Version:</strong> {{ version }}
            </div>
            <p>Welcome to your digital surfboard shaper guide. Understand shapes, sizes, and what they do!</p>
            {% for board in boards %}
            <div class="board">
                <h3>{{ board.name }}</h3>
                <p><strong>Size:</strong> {{ board.size }}</p>
                <p><strong>Shape:</strong> {{ board.shape }}</p>
                <p><strong>Best For:</strong> {{ board.best_for }}</p>
            </div>
            {% endfor %}
        </div>
    </body>
    </html>
    """, boards=SURFBOARDS, env=env, version=version)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
