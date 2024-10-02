from flask import Flask, render_template, url_for, flash, redirect, request
from flask_mail import Mail, Message


app = Flask(__name__)
app.secret_key = '1234'  

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'punitsinha495@gmail.com'  
app.config['MAIL_PASSWORD'] = 'yhih rgyj nkkl sunj'  
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


shoes = [
    {
        "id": 1,
        "name": "Airforce1",
        "description": "Taking height and craft to new levels, the Nike Air Force 1 Sage Low re-imagines classic hoops styleby and for women.A clean leather upper is easy to style.The sculpted collar reduces hot spots.And its platform midsole adds unflinching boldness because we know: you're not just in the game, you're leading it.",
        "price": "1,600",
        "images": ["Af 1 1600.JPG", "Af1.JPG", "Af11600.JPG"]  
    },
    {
        "id": 2,
        "name": "Dunk Low Retro Unisex Shoes",
        "description": "Step into timeless style with the Dunk Low Retro Unisex Shoes. These classic sneakers offer a perfect blend of heritage design and modern comfort, making them ideal for any occasion. Featuring a low-profile silhouette, they are crafted with premium leather and durable materials to ensure long-lasting wear. The padded collar and tongue provide extra cushioning for all-day comfort, while the perforated toe box enhances breathability. With a versatile colorway, these shoes effortlessly complement any outfit, whether you’re hitting the streets or hanging out with friends. The iconic Swoosh and retro-inspired details complete the look, giving you a piece of sneaker history in every step.",
        "price": "2,000",
        "images": ["Dunk panda 2000.WEBP", "Dunk panda 2000 2.WEBP"]
    },
    {
        "id": 3,
        "name": "Jordan Air",
        "description": "The Jordan Air series is a symbol of performance, style, and innovation, combining iconic design with cutting-edge technology. Crafted for those who seek both fashion and function, these shoes offer superior cushioning with the signature Air-Sole unit, delivering unparalleled comfort and impact protection. The upper materials vary across models, ranging from premium leather to breathable mesh, ensuring a perfect fit for any lifestyle. The Jordan Air features bold designs, often showcasing the iconic Jumpman logo and other heritage details that pay tribute to the basketball legend Michael Jordan. With sleek lines, eye-catching colorways, and the latest performance features, these shoes are perfect for athletes, sneakerheads, and anyone looking to elevate their streetwear game. Whether you’re on the court or off, the Jordan Air Shoes deliver lasting comfort and timeless appeal.",
        "price": "2,000",
        "images": ["jordan-air-jordan-1-retro-high-og-chicago-lost-and-found_18316489_45637604_1000.webp", "jordan-air-jordan-1-retro-high-og-chicago-lost-and-found_18316489_45638485_1000.webp", "jordan-air-jordan-1-retro-high-og-chicago-lost-and-found_18316489_45638492_1000.webp", "jordan-air-jordan-1-retro-high-og-chicago-lost-and-found_18316489_45638527_1000.webp"]
    },
    {
        "id": 4,
        "name": "Converse Black",
        "description": "The Converse Black Shoes offer a timeless and versatile design, perfect for everyday wear. Crafted with a durable canvas upper, these shoes provide a snug, comfortable fit while maintaining breathability. The signature white rubber toe cap and vulcanized rubber sole offer durability and iconic Converse style, ensuring grip and traction. With their sleek, minimalist black color, these shoes effortlessly complement any outfit, making them ideal for casual outings, skateboarding, or adding a touch of laid-back cool to your look. The high-quality stitching and metal eyelets enhance both durability and design, giving them a classic yet edgy appeal",
        "price": "1,000",
        "images": ["metro-fusion-converse-chuck-taylor-all-star-hi-top-black-3-5-m-5-5-w-m9160-shoes-948_1400x1400.webp"]
    },
    {
        "id": 5,
        "name": "Jordan 1 High Spider-Man",
        "description": "The Air Jordan 1 High Spider-Man is a striking tribute to the superhero world, blending the iconic design of the Jordan 1 with details inspired by Spider-Man’s universe. With a bold mix of red, black, and white on the premium leather upper, these sneakers pay homage to Spider-Man's classic suit. Unique spotted patterns on the red overlays mimic the comic book-style webbing, while the translucent icy blue outsole adds a modern twist. Complete with the signature Nike Air branding and the iconic Wings logo on the collar, the Air Jordan 1 Spider-Man delivers both style and performance, capturing the essence of a hero’s journey while staying true to its basketball heritage. These kicks are perfect for collectors, sneaker enthusiasts, and Spider-Man fans alike.",
        "price": "2,100",
        "images": ["Spider 2100.JPG", "pinterestdownloader.com-1727612213.688505.jpg", "pinterestdownloader.com-1727612257.836546.jpg"]
    },
    {
        "id": 6,
        "name": "Jordan 1 Retro High University Blue",
        "description": "The Air Jordan 1 Retro High University Blue brings a fresh and vibrant take on the classic silhouette with a nod to Michael Jordan’s college roots. Crafted with premium leather and soft suede, this pair features the iconic University Blue overlays, paired with black accents on the Swoosh, collar, and laces for a bold contrast. The crisp white leather base complements the light blue tones, creating a clean and sleek look. Equipped with Nike Air cushioning for all-day comfort and support, these sneakers are a perfect blend of performance and style. The timeless Air Jordan Wings logo and Nike branding finish off the design, making the University Blue a must-have for collectors and fans of the Air Jordan legacy.",
        "price": "2,100",
        "images": ["s-l1600.webp", "/s-l960 (1).webp", "s-l960 (2).webp", "s-l960.webp"]
    },
    {
        "id": 7,
        "name": "Jordan 1 low bred toe",
        "description": "The Air Jordan 1 Low Bred Toe combines the classic Jordan silhouette with the iconic Bred colorway for a fresh, low-top look. Featuring a premium leather upper, the sneaker boasts bold black panels, rich varsity red accents on the toe box and heel, and crisp white side panels, creating a timeless contrast. The low-cut design offers a more casual, versatile wear, while the Air-cushioned sole ensures all-day comfort and support. Complete with the iconic Nike Swoosh, Jumpman logo on the tongue, and the Wings logo on the heel, these sneakers bring together style, heritage, and performance. Perfect for those who want a blend of athletic functionality and street-ready aesthetics, the Bred Toe is a must-have for sneakerheads and Jordan fans.",
        "price": "2,100",
        "images": ["IMG_9201.JPG", "IMG_9202.JPG", 'IMG_9203.JPG', 'IMG_9204.JPG']
    }
]

@app.route('/')
def home():
    return render_template('index.html', shoes=shoes)

@app.route('/product/<int:product_id>')
def product(product_id):
    
    product = next((shoe for shoe in shoes if shoe['id'] == product_id), None)

    
    if product is None:
        return "Product not found", 404

    
    return render_template('product.html', product=product)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        email = request.form['email']
        message = request.form['message']

    
        msg = Message('New Contact Message from LazeUp',
                      sender=email,
                      recipients=['punitsinha495@gmail.com'])  
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
