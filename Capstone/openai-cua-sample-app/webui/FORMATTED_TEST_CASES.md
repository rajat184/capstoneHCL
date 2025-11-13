# Formatted Test Cases for Instruction Box

Copy and paste each test case individually into the instruction box in the UI.

---

## Test Case 1: Valid Login Test

**Test Case Number:** 1001.1.1.1  
**Description:** Valid Login Test - Verify that a valid user can log in successfully

**Steps:**
- Load https://www.saucedemo.com/v1/
- When the login page appears, type the username 'standard_user'
- Type the password 'secret_sauce'
- Click on the Login button
- Wait for the Products page to fully load
- Verify that the header "Products" appears correctly
- Verify that all items are visible

**Validation:**  
TestCase Number - 1001.1.1.1, Valid Login Test: Verify that a valid user can log in successfully.  
Tell us if this test case is passed or failed? Update the result in one word (Pass/Fail) in report against this test case number.

---

## Test Case 2: Invalid Password Test

**Test Case Number:** 1001.1.1.2  
**Description:** Invalid Password Test - Ensure incorrect credentials produce an appropriate error message

**Steps:**
- Load https://www.saucedemo.com/v1/
- When the login page appears, type the username 'standard_user'
- Enter an incorrect password such as 'wrong_pass'
- Click on the Login button
- Observe the result
- Verify that an error message appears: "Epic sadface: Username and password do not match any user in this service"

**Validation:**  
TestCase Number - 1001.1.1.2, Invalid Password Test: Ensure incorrect credentials produce an appropriate error message.  
Tell us if this test case is passed or failed? Update the result in one word (Pass/Fail) in report against this test case number.

---

## Test Case 3: Blank Login Fields Test

**Test Case Number:** 1001.1.1.3  
**Description:** Blank Login Fields Test - Verify that empty fields trigger validation errors

**Steps:**
- Load https://www.saucedemo.com/v1/
- Leave both Username and Password fields blank
- Click on the Login button
- Check if an error message appears indicating that the username is required

**Validation:**  
TestCase Number - 1001.1.1.3, Blank Login Fields Test: Verify that empty fields trigger validation errors.  
Tell us if this test case is passed or failed? Update the result in one word (Pass/Fail) in report against this test case number.

---

## Test Case 4: Add Single Product Test

**Test Case Number:** 1001.1.1.4  
**Description:** Add Single Product Test - Ensure individual products can be added successfully to the cart

**Steps:**
- Login using 'standard_user' and 'secret_sauce'
- Once on the Products page, find "Sauce Labs Backpack"
- Click 'ADD TO CART' for the backpack
- Open the shopping cart icon in the top-right corner
- Verify that the backpack appears in the cart with the correct name and price

**Validation:**  
TestCase Number - 1001.1.1.4, Add Single Product Test: Ensure individual products can be added successfully to the cart.  
Tell us if this test case is passed or failed? Update the result in one word (Pass/Fail) in report against this test case number.

---

## Test Case 5: Add Multiple Products Test

**Test Case Number:** 1001.1.1.5  
**Description:** Add Multiple Products Test - Ensure multiple products can be added to cart simultaneously

**Steps:**
- Login with 'standard_user' and 'secret_sauce'
- Add "Sauce Labs Backpack" to the cart
- Add "Sauce Labs Bike Light" to the cart
- Add "Sauce Labs Bolt T-Shirt" to the cart
- Click on the cart icon to review added items
- Verify that all selected products are displayed with accurate names and prices

**Validation:**  
TestCase Number - 1001.1.1.5, Add Multiple Products Test: Ensure multiple products can be added to cart simultaneously.  
Tell us if this test case is passed or failed? Update the result in one word (Pass/Fail) in report against this test case number.

---

## Test Case 6: Remove Product Test

**Test Case Number:** 1001.1.1.6  
**Description:** Remove Product Test - Verify that users can remove products from their cart successfully

**Steps:**
- Login with valid credentials 'standard_user' and 'secret_sauce'
- Add a product to the cart
- Open the cart page
- Click the 'REMOVE' button next to the item
- Verify that the product disappears from the cart
- Verify that the cart badge updates correctly

**Validation:**  
TestCase Number - 1001.1.1.6, Remove Product Test: Verify that users can remove products from their cart successfully.  
Tell us if this test case is passed or failed? Update the result in one word (Pass/Fail) in report against this test case number.

---

## Test Case 7: Sort Low to High Test

**Test Case Number:** 1001.1.1.7  
**Description:** Sort Low to High Test - Verify sorting functionality for ascending price order

**Steps:**
- Login to the application successfully using 'standard_user' and 'secret_sauce'
- On the Products page, locate and select the sort dropdown
- Choose 'Price (low to high)' option
- Check the product order
- Verify that items are sorted in ascending order by price

**Validation:**  
TestCase Number - 1001.1.1.7, Sort Low to High Test: Verify sorting functionality for ascending price order.  
Tell us if this test case is passed or failed? Update the result in one word (Pass/Fail) in report against this test case number.

---

## Test Case 8: Sort High to Low Test

**Test Case Number:** 1001.1.1.8  
**Description:** Sort High to Low Test - Verify sorting functionality for descending price order

**Steps:**
- Login successfully using 'standard_user' and 'secret_sauce'
- Select 'Price (high to low)' from the sort dropdown menu
- Ensure that products rearrange in descending order by price
- Verify the sorting is correct

**Validation:**  
TestCase Number - 1001.1.1.8, Sort High to Low Test: Verify sorting functionality for descending price order.  
Tell us if this test case is passed or failed? Update the result in one word (Pass/Fail) in report against this test case number.

---

## Test Case 9: Product Detail Page Test

**Test Case Number:** 1001.1.1.9  
**Description:** Product Detail Page Test - Verify that each product's details are displayed correctly

**Steps:**
- Login and navigate to the Products page using 'standard_user' and 'secret_sauce'
- Click on a product name such as "Sauce Labs Backpack"
- Check that product detail page opens
- Verify the page shows correct description
- Verify the page shows correct image
- Verify the page shows correct price

**Validation:**  
TestCase Number - 1001.1.1.9, Product Detail Page Test: Verify that each product's details are displayed correctly.  
Tell us if this test case is passed or failed? Update the result in one word (Pass/Fail) in report against this test case number.

---

## Test Case 10: Checkout Process Test

**Test Case Number:** 1001.1.1.10  
**Description:** Checkout Process Test - Ensure successful order completion with valid details

**Steps:**
- Login using 'standard_user' and 'secret_sauce'
- Add an item to the cart
- Go to cart and click on 'CHECKOUT'
- Enter valid user details:
  * First Name: Rajat
  * Last Name: Jaiswal
  * Postal Code: 110053
- Click 'CONTINUE'
- Click 'FINISH' to complete checkout
- Verify that a confirmation message "THANK YOU FOR YOUR ORDER" appears

**Validation:**  
TestCase Number - 1001.1.1.10, Checkout Process Test: Ensure successful order completion with valid details.  
Tell us if this test case is passed or failed? Update the result in one word (Pass/Fail) in report against this test case number.

---

## Test Case 11: Logout Test

**Test Case Number:** 1001.1.1.11  
**Description:** Logout Test - Verify logout functionality returns user to login page securely

**Steps:**
- Login successfully using 'standard_user' and 'secret_sauce'
- Click on the menu (≡) icon in the top-left corner
- Click on 'LOGOUT'
- Ensure you are redirected back to login page
- Verify logout was successful

**Validation:**  
TestCase Number - 1001.1.1.11, Logout Test: Verify logout functionality returns user to login page securely.  
Tell us if this test case is passed or failed? Update the result in one word (Pass/Fail) in report against this test case number.

---

## Test Case 12: Continue Shopping Test

**Test Case Number:** 1001.1.1.12  
**Description:** Continue Shopping Test - Verify that user can return to product page from cart view

**Steps:**
- Login with valid credentials 'standard_user' and 'secret_sauce'
- Add a product to the cart
- Click on cart icon
- On the cart page, click 'Continue Shopping'
- Verify that you are navigated back to the Products page

**Validation:**  
TestCase Number - 1001.1.1.12, Continue Shopping Test: Verify that user can return to product page from cart view.  
Tell us if this test case is passed or failed? Update the result in one word (Pass/Fail) in report against this test case number.

---

## Test Case 13: Cart Badge Count Test

**Test Case Number:** 1001.1.1.13  
**Description:** Cart Badge Count Test - Verify cart badge updates correctly for added items

**Steps:**
- Login with valid credentials 'standard_user' and 'secret_sauce'
- Add multiple products to the cart
- Verify the cart icon shows the correct count
- If cart shows incorrect count, note as failed

**Validation:**  
TestCase Number - 1001.1.1.13, Cart Badge Count Test: Verify cart badge updates correctly for added items.  
Tell us if this test case is passed or failed? Update the result in one word (Pass/Fail) in report against this test case number.

---

## Test Case 14: Locked Out User Test

**Test Case Number:** 1001.1.1.14  
**Description:** Locked Out User Test - Verify locked-out user cannot access the application

**Steps:**
- Load https://www.saucedemo.com/v1/
- Login with 'locked_out_user' as username
- Enter 'secret_sauce' as password
- Click on Login button
- Observe the response
- Verify that error message appears saying the user has been locked out

**Validation:**  
TestCase Number - 1001.1.1.14, Locked Out User Test: Verify locked-out user cannot access the application.  
Tell us if this test case is passed or failed? Update the result in one word (Pass/Fail) in report against this test case number.

---

## Test Case 15: Social Media Link Test

**Test Case Number:** 1001.1.1.15  
**Description:** Social Media Link Test - Verify footer social links open correct destinations

**Steps:**
- Login successfully using 'standard_user' and 'secret_sauce'
- Scroll to the bottom of Products page
- Click on Twitter icon in footer
- Verify Twitter page opens correctly
- Click on Facebook icon in footer
- Verify Facebook page opens correctly
- Click on LinkedIn icon in footer
- Verify LinkedIn page opens correctly

**Validation:**  
TestCase Number - 1001.1.1.15, Social Media Link Test: Verify footer social links open correct destinations.  
Tell us if this test case is passed or failed? Update the result in one word (Pass/Fail) in report against this test case number.

---

## How to Use

1. **Copy one test case at a time** from above
2. **Paste into the Instructions box** in the Web UI
3. **Click "Send"** to execute
4. **Wait for completion** - the system will automatically save results
5. **View report** using: `python webui/view_report.py`
6. **Repeat** for the next test case

## Important Notes

✅ Execute **one test case per submission**  
✅ The system **automatically detects** test case numbers  
✅ Results are **saved to JSON** in `webui/test_reports/`  
✅ Each test includes the **validation statement** needed for Pass/Fail detection  
✅ Screenshots and terminal output are **captured automatically**
