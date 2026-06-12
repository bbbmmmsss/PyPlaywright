from playwright.sync_api import Page,expect

def test_login(page: Page):
    #1. Launch Application

    page.goto("https://sauce-demo.myshopify.com/account/login")
    #2. Login

    page.fill('input[type="email"]', "smftest21@gmail.com")
    page.fill('input[type="password"]', "Smf@123")

    page.locator("//input[@value='Sign In']").click()

    #page.wait_for_load_state("networkidle")
    page.wait_for_timeout(10000)

    # Navigate to home page
    page.goto("https://sauce-demo.myshopify.com/")

    # 3. Search Product
    search_box = page.locator("//input[@id='search-field']").first

    search_box.wait_for(state="visible", timeout=10000)
    search_box.fill("Gray Jacket")

    # Press Enter
    search_box.press("Enter")

    # Wait for search results
    page.wait_for_load_state("networkidle")

    # Verify product appears in results
    expect(page.locator("body")).to_contain_text("Gray Jacket")

    print("Showing results for Gray Jacket")

    # # Open Product
    # page.get_by_text("Gray Jacket", exact=False).first.click()
    # # Wait for product page
    # page.wait_for_load_state("domcontentloaded")
    #
    # # 4.Add Product to Cart
    # page.locator("//input[@id='add']").first.click(timeout=20000)
    #
    # add_to_cart = page.get_by_role("button", name="Add to cart")
    #
    # expect(add_to_cart).to_be_visible(timeout=10000)
    # add_to_cart.click()
    #
    # # Wait for cart update
    # page.wait_for_load_state("networkidle")
    #
    # # Open Cart
    # page.goto("https://sauce-demo.myshopify.com/cart")

    # Verify product is present in cart
    # expect(page.locator("body")).to_contain_text("Gray Jacket")
    # page.wait_for_load_state("networkidle")
    #
    # #Complete Checkout Process
    #
    # checkout_btn = page.locator(
    #     "button[name='checkout'], "
    #     "input[name='checkout'], "
    #     "button:has-text('Check out'), "
    #     "a:has-text('Checkout')"
    # ).first
    #
    # expect(checkout_btn).to_be_visible(timeout=15000)
    # checkout_btn.click()
    #
    #
    # # Wait for checkout page
    # page.wait_for_load_state("domcontentloaded")
    #
    # print("Navigated to checkout page")
    #
    # # Fill Checkout Details (sample data)
    #
    # try:
    #     page.locator("input[name='checkout[email]']").fill(
    #         "smftest21@gmail.com"
    #     )
    #     page.locator("input[name='checkout[shipping_address][country]']").fill(
    #         "India"
    #     )
    #
    #     page.locator("input[name='checkout[shipping_address][first_name]']").fill(
    #         "Bhagyashree"
    #     )
    #
    #     page.locator("input[name='checkout[shipping_address][last_name]']").fill(
    #         "Sawant"
    #     )
    #
    #     page.locator("input[name='checkout[shipping_address][address1]']").fill(
    #         "SB Road"
    #     )
    #     page.locator("input[name='checkout[shipping_address][city]']").fill(
    #     "Pune"
    #     )
    #     page.locator("input[name='checkout[shipping_address][state]']").fill(
    #     "Maharashtra"
    #     )
    #     page.locator("input[name='checkout[shipping_address][zip]']").fill(
    #     "411016"
    #     )
    #     page.locator("input[name='checkout[shipping_address][phone]']").fill(
    #     "8208856902"
    #     )
    # except Exception:
    #     print("Checkout fields may differ on this Shopify theme")
    #
    #     # Shipping Method
    #     shipping_method = page.get_by_text(
    #         "International Shipping"
    #     )
    #     if shipping_method.count() > 0:
    #         shipping_method.click()
    #
    #     page.get_by_role("button").filter(
    #         has_text="Continue"
    #     ).click()
    #
    #     page.wait_for_load_state("networkidle")
    #
    #     # Payment Section
    #
    #     expect(page.locator("body")).to_contain_text("Payment")
    #     # Select Credit Card
    #     page.get_by_text("Credit card").click()
    #
    #     # Shopify Bogus Gateway Test Card
    #     # Payment fields are usually inside iframes
    #
    #     card_number_frame = page.frame_locator(
    #         "iframe[name*='card-fields-number']"
    #     )
    #
    #     card_number_frame.locator(
    #         "input"
    #     ).fill("1")
    #     expiry_frame = page.frame_locator(
    #         "iframe[name*='card-fields-expiry']"
    #     )
    #
    #     expiry_frame.locator(
    #         "input"
    #     ).fill("01/30")
    #
    #     cvv_frame = page.frame_locator(
    #         "iframe[name*='card-fields-verification_value']"
    #     )
    #
    #     cvv_frame.locator(
    #         "input"
    #     ).fill("123")
    #
    #     name_frame = page.frame_locator(
    #         "iframe[name*='card-fields-name']"
    #     )
    #
    #     name_frame.locator(
    #         "input"
    #     ).fill("Bhagyashree Sawant")
    #
    #     # Billing Address
    #     page.get_by_text(
    #         "Use a new address"
    #     ).click()
    #
    #     page.locator("input[name*='billing_address'][name*='first_name']").fill(
    #         "Bhagyashree"
    #     )
    #
    #     page.locator("input[name*='billing_address'][name*='last_name']").fill(
    #         "Sawant"
    #     )
    #
    #     page.locator("input[name*='billing_address'][name*='address1']").fill(
    #         "Dangat Patil Nagar Pune"
    #     )
    #
    #     page.locator("input[name*='billing_address'][name*='city']").fill(
    #         "Pune"
    #     )
    #
    #     page.locator("input[name*='billing_address'][name*='postal']").fill(
    #         "411023"
    #     )
    #
    #     page.locator("input[name*='billing_address'][name*='phone']").fill(
    #         "8208856902"
    #     )
    #
    #     # Complete Order
    #     page.get_by_role("button").filter(
    #         has_text="Pay now"
    #     ).click()
    #
    #     # Verify Successful Order Placement
    #     expect(page.locator("body")).to_contain_text(
    #         "Thank you,Bhagyashree"
    #     )
    #
    #     print("Your order is confirmed")
    #
    #
    #
    #
    #
    #
