# Flask Blog Application

## Description
This project is a blog application built using the Flask framework. It fetches blog posts from an external API, displays them on the website, and allows users to contact the blog owner via a contact form. The application also sends an email notification to the blog owner when a new message is received.

# Features
Fetch Blog Posts: Retrieves blog posts from an external API and displays them on the homepage.

Formatted Dates: Converts and formats the dates of the blog posts for display.

Contact Form: Provides a contact form for users to send messages to the blog owner.

Email Notifications: Sends an email notification to the blog owner when a new message is received via the contact form.

Dynamic Routing: Uses dynamic routing to display individual blog posts based on their ID.

# How It Works
Load Environment Variables: Loads email credentials and other configuration settings from environment variables.

Fetch Blog Posts: Sends a GET request to an external API to fetch blog posts and formats the dates for display.

Define Routes: Sets up routes for the homepage, about page, contact page, and individual blog posts.

Render Templates: Uses Flask's render_template function to render HTML templates with the fetched data.

Handle Contact Form: Processes the contact form submissions, sends an email notification, and displays a confirmation page.
