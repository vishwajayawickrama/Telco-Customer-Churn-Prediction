# Business Impact Analysis

This analysis connects churn prediction insights to **business outcomes**, grounded in the results of the **Chi-Square tests, t-test, and distributional analysis** from the Telco Customer Churn dataset.

---

## 5.1 Customer Segmentation for Retention

We segment customers into **High-Risk, Medium-Risk, and Low-Risk churn groups** using EDA statistical tests.

---

### High-Risk Segment (Churn Probability > 0.7)

**Statistical Evidence:**

* **Contract Type (χ² = 57.54, p < 0.001)**

  * Month-to-month contract customers: **42.7% churn rate**.
  * One-year contract: **11.3% churn rate**.
  * Two-year contract: **2.8% churn rate**.
    → Customers on month-to-month contracts are overwhelmingly more likely to churn.

* **Payment Method (χ² significant, p < 0.01)**

  * Electronic check users had the **highest churn rate** (\~45%).
  * Bank transfer and credit card auto-pay methods saw churn rates <20%.
    → Customers using electronic checks represent a critical high-risk group.

* **Internet Service (χ² = 35.06, p < 0.001)**

  * Fiber optic customers: **41.9% churn rate**.
  * DSL customers: **19% churn rate**.
  * No internet service: **7.4% churn rate**.
    → Fiber optic users show significant dissatisfaction or cost sensitivity.

* **OnlineSecurity and TechSupport (χ² > 38, p < 0.001)**

  * No add-on service: \~42% churn.
  * With add-on service: <15% churn.
    → Lack of value-added services is a churn accelerator.

* **Tenure (t-test, p < 0.001)**

  * Mean tenure of churned customers: **17.9 months**.
  * Mean tenure of non-churned customers: **37.6 months**.
    → Short-tenure customers are at high risk.

**Business Implications:**

* These customers are disengaged, price-sensitive, and uncommitted.
* Immediate intervention needed to avoid direct revenue loss.

---

### Medium-Risk Segment (Churn Probability 0.4–0.7)

**Statistical Evidence:**

* **One-Year Contracts**

  * Churn rate: \~11%, higher than two-year but lower than month-to-month.
    → At-risk but less severe.

* **DSL Customers Without Add-Ons**

  * Moderate churn (\~20–25%).
    → Lack of complementary services reduces stickiness.

* **MonthlyCharges**

  * Mid-range (60–80 USD) customers show moderate churn compared to very low or high charges.
    → These customers may not see proportional value for cost.

* **Paperless Billing (χ² = 7.04, p < 0.01)**

  * Customers with paperless billing: \~33.6% churn.
  * Customers without: \~16.3% churn.
    → Indicates billing format affects engagement.

**Business Implications:**

* These customers can be retained with targeted engagement.
* Without intervention, they may migrate to high-risk group.

---

### Low-Risk Segment (Churn Probability < 0.4)

**Statistical Evidence:**

* **Two-Year Contracts**

  * Churn rate only 2.8%.
    → Contract length locks in loyalty.

* **Automatic Payments**

  * Bank transfer / credit card: <15% churn.
    → Customers tied into auto-pay show financial and behavioral commitment.

* **Long Tenure (>36 months)**

  * Very low churn.
    → Long-term customers are loyal and less price-sensitive.

**Business Implications:**

* Minimal retention spend required.
* Strong potential for **upselling and cross-selling** premium services.

---

## 5.2 Retention Strategy Recommendations

### Targeted Interventions

* **High-Risk Customers**

  * Convert **month-to-month to annual/two-year contracts** with discounts.
  * Incentivize **switch from electronic check to auto-pay**.
  * Provide **Fiber optic bundles** (e.g., add streaming or security at reduced rate).
  * Offer free or trial access to **OnlineSecurity/TechSupport** to increase stickiness.

* **Medium-Risk Customers**

  * Launch **loyalty rewards** at 12–18 months tenure (most vulnerable period).
  * Provide personalized offers for **add-on services** at discounted rates.
  * Use **paperless billing nudges** with added benefits (eco-discounts).

* **Low-Risk Customers**

  * Upsell: higher speed internet, premium streaming, device insurance.
  * Maintain loyalty with **non-financial perks** (priority support, early access).

---

### Resource Allocation

* **70% of retention budget** → High-Risk (confirmed by χ² significance and t-test).
* **20%** → Medium-Risk (prevent escalation).
* **10%** → Low-Risk (focus on upsell).

---

### Expected ROI

* Preventing churn in **month-to-month + electronic check users** saves the largest recurring revenue share.
* Retaining **senior citizens and short-tenure customers** prevents high acquisition replacement costs.
* Upselling loyal customers increases ARPU without new acquisition costs.

---

## 5.3 References to Statistical Tests

* **Chi-Square Test**:

  * Significant: SeniorCitizen, Partner, Dependents, Contract, PaymentMethod, InternetService, OnlineSecurity, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, PaperlessBilling.
  * Not significant: Gender, PhoneService, MultipleLines.

* **T-Test**:

  * Tenure significantly different between churned vs non-churned (p < 0.001).

* **Business Insight**:

  * Retention focus should **not** waste resources on non-significant factors (Gender, PhoneService).
  * Maximum ROI comes from addressing statistically confirmed churn drivers.

