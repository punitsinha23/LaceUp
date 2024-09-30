from flask import Flask, render_template, url_for, flash, redirect, request
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Ensure you set a secret key for flashing messages

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'punitsinha495@gmail.com'  # Replace with your Gmail address
app.config['MAIL_PASSWORD'] = 'yhih rgyj nkkl sunj'  # Use App-specific password generated from Gmail
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

# Dummy data for shoes
shoes = [
    {
        "id": 1,
        "name": "Airforce1",
        "description": "Taking height and craft to new levels, the Nike Air Force 1 Sage Low re-imagines classic hoops styleby and for women.A clean leather upper is easy to style.The sculpted collar reduces hot spots.And its platform midsole adds unflinching boldness because we know: you're not just in the game, you're leading it.",
        "price": "1,600",
        "images": ["Af 1 1600.JPG", "Af1.JPG", "Af11600.JPG"]  # Add multiple images
    },
    {
        "id": 2,
        "name": "Dunk Low Retro Unisex Shoes",
        "description": "This is a description for shoe 2.",
        "price": "2,000",
        "images": ["Dunk panda 2000.WEBP", "Dunk panda 2000 2.WEBP"]
    },
    {
        "id": 3,
        "name": "Jordan Air",
        "description": "This is a description for shoe 3.",
        "price": "2,000",
        "images": ["jordan-air-jordan-1-retro-high-og-chicago-lost-and-found_18316489_45637604_1000.webp", "jordan-air-jordan-1-retro-high-og-chicago-lost-and-found_18316489_45638485_1000.webp", "jordan-air-jordan-1-retro-high-og-chicago-lost-and-found_18316489_45638492_1000.webp", "jordan-air-jordan-1-retro-high-og-chicago-lost-and-found_18316489_45638527_1000.webp"]
    },
    {
        "id": 4,
        "name": "Converse Black",
        "description": "This is a description for shoe 4.",
        "price": "1,000",
        "images": ["metro-fusion-converse-chuck-taylor-all-star-hi-top-black-3-5-m-5-5-w-m9160-shoes-948_1400x1400.webp"]
    },
    {
        "id": 5,
        "name": "Jordan 1 High Spider-Man",
        "description": "This is a description for shoe 5.",
        "price": "2,000",
        "images": ["Spider 2100.JPG", "pinterestdownloader.com-1727612213.688505.jpg", "pinterestdownloader.com-1727612257.836546.jpg"]
    },
    {
        "id": 6,
        "name": "Jordan 1 Retro High University Blue",
        "description": "This is a description for shoe 6.",
        "price": "2,000",
        "images": ["s-l1600.webp", "/s-l960 (1).webp", "s-l960 (2).webp", "s-l960.webp"]
    }
]

@app.route('/')
def home():
    return render_template('index.html', shoes=shoes)

@app.route('/product/<int:product_id>')
def product(product_id):
    # Retrieve the product from the list using the product_id
    product = next((shoe for shoe in shoes if shoe['id'] == product_id), None)

    # Check if the product exists, otherwise return a 404 page
    if product is None:
        return "Product not found", 404

    # Pass the product to the template
    return render_template('product.html', product=product)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        email = request.form['email']
        message = request.form['message']

        # Send email to your inbox
        msg = Message('New Contact Message from LazeUp',
                      sender=email,
                      recipients=['punitsinha495@gmail.com'])  # Your email to receive messages
        msg.body = f"Message from {email}:\n\n{message}"
        
        try:
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
        except Exception as e:
            flash(f'Failed to send email. Error: {str(e)}', 'danger')

        return redirect(url_for('contact'))

    return render_template('contact.html')

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
