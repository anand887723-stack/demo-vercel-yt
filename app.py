from flask import Flask, request, jsonify
# from twilio.twiml.messaging_response import MessagingResponse
import data_loader

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "ki chol che anand bhai "

@app.route('/menu', methods=['POST'])
def menu():
    # Retrieve the message content from the request JSON
    incoming_msg = request.json.get('message', '').lower()  # Expecting JSON body with {"message": "monday dinner"}
    print(f"Received message: {incoming_msg}")

    # Split the message into parts
    parts = incoming_msg.split()
    if len(parts) == 2:
        day, meal = parts
        menu_items = data_loader.get_menu(day, meal)

        # Format the response message
        if isinstance(menu_items, list):
            menu_response = f"{day.capitalize()} {meal.capitalize()} menu:\n" + "\n".join(menu_items)
        else:
            menu_response = menu_items
    else:
        # Default response for unrecognized format
        menu_response = 'Please provide a valid input in the format "day meal" (e.g., "monday dinner").'

    # Return the response as JSON
    return jsonify({"response": menu_response})

if __name__ == '__main__':
    app.run(debug=True)


