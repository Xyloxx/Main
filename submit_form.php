<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    
    // Collect form data
    $friend_email = $_POST['friend_email'];
    $your_name = $_POST['your_name'];
    $message = $_POST['message'];

    // Assuming you want to send an email:
    $to = $friend_email;
    $subject = "You've been invited to join Zero Marketplace by $your_name!";
    $headers = "From: noreply@zeromarketplace.com" . "\r\n" .
    "Reply-To: noreply@zeromarketplace.com" . "\r\n" .
    "X-Mailer: PHP/" . phpversion();

    $email_message = "
    Hi,

    $your_name has invited you to join Zero Marketplace!
    
    " . (!empty($message) ? "Here's a message from $your_name: $message" : "") . "

    Click the link below to sign up:
    [Link to your signup page]

    Regards,
    Zero Marketplace Team
    ";

    // Send the email
    if (mail($to, $subject, $email_message, $headers)) {
        echo "Invite sent successfully!";
    } else {
        echo "Failed to send the invite.";
    }
} else {
    // Not a POST request
    echo "Invalid request.";
}
?>
