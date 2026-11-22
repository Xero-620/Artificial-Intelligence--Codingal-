MENU = {

"pizza": 950, "pasta": 420, "burger": 880, "fries": 760, "tacos": 310,

"sushi": 280, "ramen": 260, "biryani": 990, "paneer tikka": 540,

"butter chicken": 610, "masala dosa": 470, "idli": 350, "samosa": 640,

"pav bhaji": 380, "momos": 720, "noodles": 590, "fried rice": 500,

"sandwich": 450, "salad": 230, "pancakes": 210, "waffles": 190,

"brownie": 330, "cake": 300, "coke": 800, "coffee": 670, "tea": 560,

"mango lassi": 400, "ice cream": 690, "milkshake": 360, "nachos": 270,

}

USE_KEYBOARD = True
USE_SWAP = True
KEY_ROWS = [
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm"]
KEY_POS = {c: (r, i) for r, row in enumerate(KEY_ROWS) for i, c in enumerate(row)}