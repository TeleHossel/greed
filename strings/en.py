# Strings / localization file for greed
# Can be edited, but DON'T REMOVE THE REPLACEMENT FIELDS (words surrounded by {curly braces})

# Currency symbol
currency_symbol = "€"

# Positioning of the currency symbol
currency_format_string = "{symbol} {value}"

# Quantity of a product in stock
in_stock_format_string = "{quantity} beschikbaar"

# Copies of a product in cart
in_cart_format_string = "{quantity} in winkelwagen"

# Product information
product_format_string = "<b>{name}</b>\n" \
                        "{description}\n" \
                        "{price}\n" \
                        "<b>{cart}</b>"

# Order number, displayed in the order info
order_number = "Bestelling #{id}"

# Order info string, shown to the admins
order_format_string = "Besteld door: {user}\n" \
                      "Besteld op: {date}\n" \
                      "\n" \
                      "{items}\n" \
                      "TOTAAL: <b>{value}</b>\n" \
                      "\n" \
                      "Locatie: {notes}\n"

# Order info string, shown to the user
user_order_format_string = "{status_emoji} <b>Bestelling {status_text}</b>\n" \
                           "{items}\n" \
                           "TOTAAL: <b>{value}</b>\n" \
                           "\n" \
                           "Locatie: {notes}\n"

# Transaction page is loading
loading_transactions = "<i>Bestellingen laden...\n" \
                       "Een moment geduld aub.</i>"

# Transactions page
transactions_page = "Pagina <b>{page}</b>:\n" \
                    "\n" \
                    "{transactions}"

# transactions.csv caption
csv_caption = "In een 📄 .csv bestand staan alle bestellingen uit de database van de bot." 

# Conversation: the start command was sent and the bot should welcome the user
conversation_after_start = "Hallo\n" \
                           "Welkom bij de TeleHossel bot\n" \
                           "Discreet en gemakkelijk je stuff bestellen!\n" \
                           "Voeg geld toe aan je wallet en bestel.\n" \
                           "Uitleg nodig over de bot? Druk op de knop BOT UITLEG"

# Conversation: to send an inline keyboard you need to send a message with it
conversation_open_user_menu = "Wat wil je doen?\n" \
                              "💰 Je hebt <b>{credit}</b> in je wallet.\n" \
                              "\n" \
                              "<i>Gebruik de knoppen in het menu om de bot te gebruiken.\n" \
                              "Is het menu niet geopend?" \
                              " Druk op de knop met de puntjes om het menu te openen.</i>"

# Conversation: like above, but for administrators
conversation_open_admin_menu = "Je bent een beheerder 💼 <b>Manager</b> van deze bot\n" \
                               "Wat wil je doen?\n" \
                               "\n" \
                               "<i>Gebruik de knoppen in het menu om de bot te gebruiken.\n" \
                               "Is het menu niet geopend?" \
                               "Druk op de knop met de puntjes om het menu te openen. </i>"

# Conversation: select a payment method
conversation_payment_method = "Druk op de knop BITCOIN om geld toe te voegen aan de wallet."

# Conversation: select a product to edit
conversation_admin_select_product = "✏️Welk product wil je bewerken?"

# Conversation: select a product to delete
conversation_admin_select_product_to_delete = "❌ Welk product wil je verwijderen?"

# Conversation: select a user to edit
conversation_admin_select_user = "Selecteer een gebruiker om te bewerken."

# Conversation: click below to pay for the purchase
conversation_cart_actions = "<i>Druk op de knop TOEVOEGEN." \
                            " Om producten in je winkelwagen te zetten. Alles toegevoegd?" \
                            " Druk op de knop OVERZICHT.</i>"

# Conversation: confirm the cart contents
conversation_confirm_cart = "🛒 De volgende producten zitten in je winkelwagen:\n" \
                            "{product_list}" \
                            "TOTAAL: <b>{total_cost}</b>\n" \
                            "\n" \
                            "<i>Om je bestelling te voltooien, druk op de knop BESTEL.\n" \
                            "Om je bestelling te annuleren, druk op de knop ANNULEREN.</i>"

# Live orders mode: start
conversation_live_orders_start = "Je ziet nu<b>Live bestellingen</b> binnenkomen\n" \
                                 "Alle bestellingen die door de klanten worden gedaan worden, worden hier live weergegeven." \
                                 " Markeer voltooide bestellingen als ✅ Voltooid" \
                                 "Of ✴️ betaal de klant terug"

# Live orders mode: stop receiving messages
conversation_live_orders_stop = "<i>Druk op de knop STOP" \
                                " om de live bestellingen te stoppen.</i>"

# Conversation: help menu has been opened
conversation_open_help_menu = "Waar heb je hulp mee nodig?"

# Conversation: confirm promotion to admin
conversation_confirm_admin_promotion = " Ben je er zeker van dat je deze gebruiker een 💼 Beheerder van de bot wilt maken? ?\n" \
                                       "Hiermee geef je de gebruiker toegang tot het beheerders menu."

# Conversation: language select menu header
conversation_language_select = "Selecteer de taal:"

# Conversation: switching to user mode
conversation_switch_to_user_mode = " Je schakelt naar het 👤 Klant menu\n" \
                                   "Als je terug wilt naar het 💼 Beheerder menu, type /start in de chatbalk."

# Notification: the conversation has expired
conversation_expired = "🕐  Ik heb al tijd geen berichten meer ontvangen. Dus ik heb de chat gesloten." \
                       " om het overzichtelijk te houden\n" \
                       "Als je een nieuwe bestelling wilt doen, type /start in de chatbalk"

# User menu: order
menu_order = "🛒 Bestel stuff"

# User menu: order status
menu_order_status = "🛍 Mijn bestellingen"

# User menu: add credit
menu_add_credit = "💵 Geld toevoegen"

# User menu: bot info
menu_bot_info = "ℹ️ Bot uitleg"

# User menu: cash
menu_cash = "💵 Contant"

# User menu: credit card
menu_credit_card = "💳 Met creditcard"

# Admin menu: products
menu_products = "📝️ Producten"

# Admin menu: orders
menu_orders = "📦 Bestellingen"

# Menu: transactions
menu_transactions = "💳 Bestellingen lijst"

# Menu: edit credit
menu_edit_credit = "💰 Overboeking maken"

# Admin menu: go to user mode
menu_user_mode = "👤 Gebruiker mode"

# Admin menu: add product
menu_add_product = "✨ Nieuw product"

# Admin menu: delete product
menu_delete_product = "❌ Verwijder product"

# Menu: cancel
menu_cancel = "🔙 Annuleren"

# Menu: skip
menu_skip = "⏭ Overslaan"

# Menu: done
menu_done = "✅️ Overzicht"

# Menu: pay invoice
menu_pay = "💳 Bestel"

# Menu: complete
menu_complete = "✅ Voltooid"

# Menu: refund
menu_refund = "✴️ Terugbetalen"

# Menu: stop
menu_stop = "🛑 Stop"

# Menu: add to cart
menu_add_to_cart = "➕ Toevoegen"

# Menu: remove from cart
menu_remove_from_cart = "➖ Verwijderen"

# Menu: help menu
menu_help = "❓ Help"

# Menu: guide
menu_guide = "📖 Uitleg"

# Menu: next page
menu_next = "▶️ Volgende"

# Menu: previous page
menu_previous = "◀️ Vorige"

# Menu: contact the shopkeeper
menu_contact_shopkeeper = "👨‍💼 Contacteer beheerder"

# Menu: generate transactions .csv file
menu_csv = "📄 .csv"

# Menu: edit admins list
menu_edit_admins = "🏵 Wijzig beheerder"

# Menu: language
menu_language = "🇳🇱 Taal"

# Emoji: unprocessed order
emoji_not_processed = "*️⃣"

# Emoji: completed order
emoji_completed = "✅"

# Emoji: refunded order
emoji_refunded = "✴️"

# Emoji: yes
emoji_yes = "✅"

# Emoji: no
emoji_no = "🚫"

# Text: unprocessed order
text_not_processed = "Verwerken"

# Text: completed order
text_completed = "Voltooid"

# Text: refunded order
text_refunded = "Terugbetaald"

# Text: product not for sale
text_not_for_sale = "Niet beschikbaar voor verkoop"

# Add product: name?
ask_product_name = "Wat moet de naam van het product zijn?"

# Add product: description?
ask_product_description = "Wat moet de beschrijving van het product zijn?"

# Add product: price?
ask_product_price = "Wat moet de prijs van het product zijn?\n" \
                    "Voer <code>X</code> in als je het product nog niet beschikbaar wilt hebben voor verkoop"

# Add product: image?
ask_product_image = "🖼 Wil je een foto van het product toevoegen?\n" \
                    "\n" \
                    "<i>Stuur de foto, of sla deze stap over.</i>"

# Order product: notes?
ask_order_notes = "Type de afleverlocatie in de chatbalk.\n" \
                  "Indien je geen voorkeur hebt voor een locatie druk op de knop OVERSLAAN.</i>"

# Refund product: reason?
ask_refund_reason = " Type reden voor terugbetaling in chatbalk.\n" \
                    "👤  De gebruiker ziet de reden."

# Edit credit: notes?
ask_transaction_notes = " Voeg een bericht toe aan deze overboeking.\n" \
                        "👤 De gebruiker ziet dit bericht" \
                        " En de 💼 Beheerder in de transactie geschiedenis."

# Edit credit: amount?
ask_credit = "Wat wil je wijzigen aan de wallet van deze gebruiker\n" \
             "\n" \
             "<i>Type in de chatbalk het aantal.\n" \
             "Gebruik het teken </i><code>+</code><i> voor toevoegen," \
             " en het teken </i><code>-</code><i> voor verwijderen.</i>"

# Header for the edit admin message
admin_properties = "<b>Rechten van {name}:</b>"

# Edit admin: can edit products?
prop_edit_products = "Wijzig producten"

# Edit admin: can receive orders?
prop_receive_orders = "Ontvang bestellingen"

# Edit admin: can create transactions?
prop_create_transactions = "Beheer transacties"

# Edit admin: show on help message?
prop_display_on_help = "Laat aan gebruiker zien"

# Thread has started downloading an image and might be unresponsive
downloading_image = "Ik ben de foto aan het downloaden!\n" \
                    "Een moment geduld aub...\n" \
                    "Tijdens het downloaden kan ik je berichten niet beantwoorden."

# Edit product: current value
edit_current_value = "De huidige waarde is:\n" \
                     "<pre>{value}</pre>\n" \
                     "\n" \
                     "<i>Druk op de knop OVERSLAAN om de huidige waarde te houden.</i>"

# Payment: cash payment info
payment_cash = "Je kan contant betalen bjj de verkoper."
               "<b>{user_cash_id}</b>"

# Payment: invoice amount
payment_cc_amount = "Hoeveel € wil je toevoegen aan je wallet?\n" \
                    "\n" \
                    "<i>Selecteer een bedrag of voer het gewenste bedrag zelf in</i>"

# Payment: add funds invoice title
payment_invoice_title = "Geld toevoegen"

# Payment: add funds invoice description
payment_invoice_description = "Na betaling word {amount} aan je wallet toegevoegd."

# Payment: label of the labeled price on the invoice
payment_invoice_label = "Opladen"

# Payment: label of the labeled price on the invoice
payment_invoice_fee_label = "Transactie kosten"

# Notification: order has been placed
notification_order_placed = "Er is een nieuwe bestelling geplaatst:\n" \
                            "\n" \
                            "{order}"

# Notification: order has been completed
notification_order_completed = "Je bestelling is voltooid.\n" \
                               "\n" \
                               "{order}"

# Notification: order has been refunded
notification_order_refunded = "Je bestelling is terugbetaald.\n" \
                              "\n" \
                              "{order}"

# Notification: a manual transaction was applied
notification_transaction_created = "ℹ️  Je hebt een overboeking ontvangen het geld is toegevoegd aan je wallet:\n" \
                                   "{transaction}"

# Refund reason
refund_reason = "Reden terugbetaling:\n" \
                "{reason}"

# Info: informazioni sul bot
bot_info = "Druk op de link in mijn bio voor uitleg"

# Help: guide
help_msg = "Voor hulp contacteer de beheerder"

# Help: contact shopkeeper
contact_shopkeeper = "Voor hulp contacteer de beheerder."

# Success: product has been added/edited to the database
success_product_edited = "✅ Het product is toegevoegd of gewijzigd!"

# Success: product has been added/edited to the database
success_product_deleted = "✅ Het product is verwijderd!"

# Success: order has been created
success_order_created = "✅ De bestelling is verzonden!\n" \
                        "\n" \
                        "{order}"

# Success: order was marked as completed
success_order_completed = "✅ Je hebt #{order_id} voltooid!"

# Success: order was refunded successfully
success_order_refunded = "✴️ Bestelling #{order_id} is terugbetaald!"

# Success: transaction was created successfully
success_transaction_created = "✅ De overboeking is verzonden!\n" \
                              "{transaction}"

# Error: message received not in a private chat
error_nonprivate_chat = "⚠️ This bot only works in private chats."

# Error: a message was sent in a chat, but no worker exists for that chat.
# Suggest the creation of a new worker with /start
error_no_worker_for_chat = "⚠️ The conversation with the bot was interrupted.\n" \
                           "To restart it, send the /start command to the bot."

# Error: a message was sent in a chat, but the worker for that chat is not ready.
error_worker_not_ready = "🕒 The conversation with the bot is currently starting.\n" \
                         "Please, wait a few moments before sending more commands!"

# Error: add funds amount over max
error_payment_amount_over_max = "⚠️ The maximum amount that can be added in a single transaction is {max_amount}."

# Error: add funds amount under min
error_payment_amount_under_min = "⚠️ The minimum amount that can be added in a single transaction is {min_amount}."

# Error: the invoice has expired and can't be paid
error_invoice_expired = "⚠️ This invoice has expired and was canceled. If you still want to add funds, use the Add" \
                        " funds menu option."

# Error: a product with that name already exists
error_duplicate_name = "️⚠️ A product with the same name already exists."

# Error: not enough credit to order
error_not_enough_credit = "⚠️ You do not have enough credit to place the order."

# Error: order has already been cleared
error_order_already_cleared = "⚠️  This order has already been processed."

# Error: no orders have been placed, so none can be shown
error_no_orders = "⚠️  You haven't placed any order yet, so there is nothing to display."

# Error: selected user does not exist
error_user_does_not_exist = "⚠️  The selected user does not exist."

# Fatal: conversation raised an exception
fatal_conversation_exception = "☢️ Oh no! An <b>error</b> interrupted this conversation\n" \
                               "The error was reported to the bot owner so that he can fix it.\n" \
                               "To restart the conversation, send the /start command again."
