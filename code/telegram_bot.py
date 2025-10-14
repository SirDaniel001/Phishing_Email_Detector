# code/telegram_bot.py
import os
import logging
import traceback
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Import your existing functions directly
import sys
import os

# Add the current directory to path
sys.path.append(os.path.dirname(__file__))

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

def escape_markdown(text):
    """Escape special characters for Telegram MarkdownV2"""
    escape_chars = r'_*[]()~`>#+-=|{}.!'
    return ''.join(['\\' + char if char in escape_chars else char for char in text])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    welcome_text = f"""
👋 Hello {user.first_name}!

I'm *PhishGuard Bot* - powered by your advanced AI phishing detection system.

🔍 *I use:*
• Machine Learning (Random Forest)
• Expert System Rules  
• Hybrid Intelligence

📧 *How to use:*
Just send me any email or message text, and I'll analyze it for phishing indicators!

Try sending me a suspicious message to test!
"""
    await update.message.reply_markdown_v2(escape_markdown(welcome_text))

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = """
🆘 *Help Guide*

*Commands:*
/start - Start the bot
/help - Show this help
/analyze [text] - Analyze specific text

*What I detect:*
• Urgency tactics ("urgent", "verify now")
• Financial incentives ("free", "win", "prize")
• Suspicious requests ("password", "click here")
• Poor grammar & excessive punctuation
• Currency amounts

*Example:*
`URGENT: Your account will be suspended! Click here to verify: bit.ly/fake-link`
"""
    await update.message.reply_markdown_v2(escape_markdown(help_text))

async def analyze_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text("Please provide text to analyze. Usage: /analyze [message text]")
        return
    
    text = ' '.join(context.args)
    await analyze_and_reply(update, text)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Show typing action
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    
    text = update.message.text
    
    # Ignore very short messages unless they contain URLs
    if len(text) < 10 and not any(keyword in text.lower() for keyword in ['http', 'www.', 'click']):
        return
    
    await analyze_and_reply(update, text)

async def analyze_and_reply(update: Update, text: str) -> None:
    """Analyze text using your hybrid system and send formatted result"""
    try:
        print(f"🔍 Analyzing message: {text[:50]}...")
        
        # Import here to avoid loading models on bot startup
        from simple_detector import simple_hybrid_predict
        
        # Use the simple prediction system
        final_pred, ai_pred, rule_trig, rules, confidence = simple_hybrid_predict(text)
        print(f"✅ Analysis successful: final_pred={final_pred}, ai_pred={ai_pred}, confidence={confidence}")
        
        # Format the result for Telegram
        result_message = format_analysis_result(text, final_pred, ai_pred, rule_trig, rules, confidence)
        
        await update.message.reply_markdown_v2(result_message)
        print("✅ Result sent to user")
        
    except Exception as e:
        logger.error(f"Error analyzing message: {e}")
        logger.error(traceback.format_exc())
        
        # Print detailed error info
        print(f"❌ ERROR DETAILS: {str(e)}")
        print(f"❌ TRACEBACK: {traceback.format_exc()}")
        
        # Send simple error message without markdown
        await update.message.reply_text("❌ Sorry, I encountered an error analyzing your message. Please try again.")

def format_analysis_result(text, final_pred, ai_pred, rule_trig, rules, confidence):
    """Format your hybrid system output for Telegram with proper escaping"""
    
    # Final result
    final_result = "🚨 PHISHING DETECTED" if final_pred == 1 else "✅ LEGITIMATE MESSAGE"
    
    # AI prediction
    ai_result = "SPAM" if ai_pred == 1 else "HAM"
    confidence_percent = f"{confidence * 100:.1f}%"
    
    # Escape the confidence percentage (it contains parentheses and dots)
    escaped_confidence = escape_markdown(confidence_percent)
    
    # Rules triggered
    rules_text = ""
    if rule_trig and rules:
        escaped_rules = [escape_markdown(rule) for rule in rules]
        rules_text = "\n🔍 *Rules Triggered:*\n" + "\n".join([f"• {rule}" for rule in escaped_rules])
    else:
        rules_text = "\n🔍 *Rules Triggered:* None"
    
    # Escape message preview
    escaped_preview = escape_markdown(text[:100] + ('...' if len(text) > 100 else ''))
    
    # Analysis details - properly escaped for MarkdownV2
    recommendation = "🚨 HIGH RISK - Do not click links or provide information" if final_pred == 1 else "✅ Likely safe - Always verify unexpected messages"
    
    analysis_details = f"""
🔍 *Phishing Analysis Complete*

*Final Verdict:* {escape_markdown(final_result)}
*AI Prediction:* {escape_markdown(ai_result)} \\({escaped_confidence} confidence\\)
{rules_text}

*Message Preview:* 
`{escaped_preview}`

💡 *Recommendation:*
{escape_markdown(recommendation)}
"""
    return analysis_details

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    logger.error(traceback.format_exc())
    if update and update.message:
        await update.message.reply_text("❌ Sorry, I encountered an error. Please try again.")

def main() -> None:
    """Start the bot"""
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not token:
        logger.error("No TELEGRAM_BOT_TOKEN found in environment variables")
        print("❌ Please set TELEGRAM_BOT_TOKEN environment variable")
        print("💡 Run: export TELEGRAM_BOT_TOKEN='your_bot_token_here'")
        return
    
    # Create application
    application = Application.builder().token(token).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("analyze", analyze_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_error_handler(error_handler)

    # Start the bot
    print("🤖 Starting Telegram bot...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
