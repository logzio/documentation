---
sidebar_position: 3
title: AI FAQ - Usage, Security, and Privacy 
description: Answers to common questions about Logz.io’s AI, including usage, security, data access, and privacy.
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [AI, observability, Assistant, iq, logs, metrics, traces, siem, insights, analysis, services, logz.io]
---

AI Agent and AI Chat are part of Logz.io’s Observability IQ suite. It helps enhance system monitoring and management by enabling an active dialogue with your data. You can access it from **[Explore](https://app.logz.io/#/dashboard/explore)**, **[Kubernetes 360](https://app.logz.io/#/dashboard/observability/k8s360)**, and **[App 360](https://app.logz.io/#/dashboard/spm/services/table)**, allowing you to transition from observing data to actively getting immediate insights on your metrics, identifying anomalies, discerning trends, and assessing the well-being of your ecosystem in real time.

## Pricing and Usage

### Why is AI usage no longer complimentary?
During our BETA period, we offered AI features at no extra cost to allow users to explore their potential. To continue providing access to the industry’s most advanced models and ensure platform stability as usage scales, we are moving to a paid usage model.

### When does this change go into effect?
Billing for AI Chat and AI Alert Analysis invocations will begin on **March 1st, 2026**. Any usage prior to this date remains complimentary.

### What is a "Token"?
* **Definition**: Tokens are the building blocks of AI processing (roughly 750 words per 1,000 tokens).
* **Billing**: We bill in units of **1 million tokens** to provide transparent and scalable pricing for high-volume users.
* **Scope**: This includes both the prompt and data you shared (input) and the AI's response (output).

### What is an "Invocation"?
An invocation is counted every time an AI Agent (like Alert Analysis) is triggered—whether via an automated alert or an API call.

### How can I estimate my future bill?
You can view your current consumption by navigating to **Settings > Admin > Plan and usage**. Under the **Usage** tab, you will find a detailed breakdown of your AI token consumption and AI agent invocations for the current billing period.

### Can I set a spending limit?
Currently, the system does not support hard spending limits for AI usage. We recommend monitoring your usage via the **Plan and usage** dashboard to stay aligned with your team's budget.

### AI Usage Pricing Table

| AI Service | Description | Volume | Price |
| :--- | :--- | :--- | :--- |
| **AI Chat** | Interactive natural language processing and generative AI assistance via chat interface | 1 Million Tokens | $10.00 |
| **AI Agents (OrionIQ)** | Specialized AI-driven task automation and data processing agents | 1 Invocation | Alert Analysis: $10.00 (Others vary) |



---

## Data Access and Privacy

### What data can the AI Agent access upon activation?​
The AI Agent activates when you enter a prompt in its interface, currently available in **[Explore](https://app.logz.io/#/dashboard/explore)**, **[Kubernetes 360](https://app.logz.io/#/dashboard/observability/k8s360)**, and **[App 360](https://app.logz.io/#/dashboard/spm/services/table)**. 

Once you provide input, the AI Agent will have access to relevant data from your Logz.io account, including all of your log data, current query, graphs, etc. This setup allows the AI Agent to interact directly with the data you're analyzing, delivering tailored insights and suggestions.

### Is my data used to train the AI model?
No. Logz.io uses the AWS Bedrock, which does not use your data for training. Your data is not shared with AWS or any third-party providers for model training purposes.

You can read more about this [here](https://aws.amazon.com/bedrock/faqs/#product-faqs#bedrock-faqs#security-and-privacy).

When generating insights, a minimal portion of your data is temporarily sent to a secure Large Language Model (LLM) instance to generate a response. Some parts of the initial prompt and the agent’s response may be stored under your account’s data retention policy. While this data is currently not used or reviewed, it may be retained longer in the future to help improve the AI Agent’s performance.

### How does the AI Agent comply with security standards?
Your data is secured using industry-standard security protocols: 
* **Data Encryption**: All data is encrypted.
* **Access Controls**: The data is processed in Logz.io’s private instance within AWS, meaning strict access controls ensure that only authorized processes can access your data, similar to the current situation where AWS processes your data. 

For more detailed information, visit Logz.io’s [security and compliance page](https://logz.io/platform/features/soc-2-compliance/). You can read more about how AWS follows best practices for data security [here](https://aws.amazon.com/bedrock/faqs/#product-faqs#bedrock-faqs#general:~:text=Why%20should%20I%20use%20Amazon%20Bedrock%3F).

### How does the AI Agent comply with Privacy and GDPR standards?​​
Your data is handled by Logz.io and AWS (being Logz.io’s sub-processor) in accordance with privacy and GDPR standards and requirements. For more detailed information, visit [Logz.io’s privacy policy](https://logz.io/about-us/privacy-policy/). You can read more about how AWS handles data protection [here](https://aws.amazon.com/bedrock/faqs/#product-faqs#bedrock-faqs#general:~:text=Why%20should%20I%20use%20Amazon%20Bedrock%3F).

### In what Geographic region is my data stored?
Logz.io aims to host the model in the same region in which you elected to store your Logz.io account data, however, due to current AWS limitations, this is not always possible:

If your data is hosted in Canada (Central), we will use the AI model hosted in `us-east-1`; and if your data is hosted in Europe (London), we will use the AI model hosted in `eu-central-1`. 

This **temporary** setup will evolve as AWS expands regional support for AI model hosting.

### Can account admins see my queries and chat history?​
No. Account admins or any other users within your organization cannot view or access any queries or chat history from the AI Agent.

### What data retention policies are in place for AI-processed information?
AI-processed data follows Logz.io’s standard data retention policies. No additional retention is introduced by the AI Agent.

### How is customer data protected when used by the AI system?
Customer data is protected through encryption, strict access controls, and private model instances hosted in Logz.io’s AWS environment. The data is never used to train models or shared with third parties.

For more details, see:
* [Security Standards](https://logz.io/platform/features/soc-2-compliance/)
* [Privacy Policy](https://logz.io/about-us/privacy-policy/)

### How are AI models protected against adversarial attacks or data poisoning attempts?
The AI models and agents are hosted on AWS Bedrock, ensuring a secure and controlled environment. 

Unauthorized data access across accounts through prompt manipulation or model exploits is prevented by multiple layers of security controls and isolation measures.

Each AI request is authenticated with the user making the request, and access is enforced to match what the user could see in the Explore/Metrics Explorer interface. 

Additionally, the models operate in a synthesis-only mode, meaning they generate responses but do not perform actions, eliminating the risk of harmful execution even in the unlikely event of a jailbreak. We use commercial LLMs (Anthropic's Claude model family) with custom context extensions, pre-aggregated data, and custom tools, ensuring controlled outputs while preventing adversarial manipulation, data leakage, or poisoning attempts.

### What controls are in place to ensure the accuracy of outputs?
Ensuring accurate outputs in AI systems relies on multiple layers of quality controls:

**1. Model Evaluation and Monitoring:**
* **Automated Evaluations**: AWS Bedrock provides tools for automatic model evaluation, assessing metrics like accuracy and robustness. These evaluations help in selecting the most suitable foundation models for specific applications.
* **Human Evaluations**: For subjective assessments, AWS Bedrock supports human evaluation workflows, allowing for nuanced judgments on model outputs.

**2. Regular Testing and Benchmarking:**
Models like Claude 3.5 Sonnet undergo rigorous testing against industry benchmarks to ensure high performance in areas such as coding, text-based reasoning, and visual interpretation.

**3. Automated Reasoning Checks:**
​​AWS applies mathematical proofs through Automated Reasoning Checks to validate that the AI behaves according to predefined rules. This helps reduce inaccuracies or "hallucinations" in model output.

**4. Continuous Monitoring and Feedback Loops:**
Ongoing monitoring and feedback mechanisms help track AI performance in real time and allow teams to detect and address inaccuracies quickly.

By integrating these controls, organizations can maintain and enhance the accuracy and reliability of AI system outputs.

In addition to model-level controls, Logz.io implements internal safeguards to maintain data integrity and output accuracy:
* **Data Integrity**: All data is encrypted using industry-standard techniques, preventing unauthorized parties from accessing or altering it.
* **Access Controls**: Strict access controls and audit logs are implemented, ensuring that only authorized personnel can access or interact with sensitive data.
* **Regular Audits**: Logz.io conducts routine security audits and uses intrusion detection systems to maintain data integrity and accuracy.

### Can the AI functions be turned off?
Yes. To disable the AI Agent on your account, contact [Logz.io support team](mailto:help@logz.io). 

### How do I provide feedback or report issues with the AI Agent?​
To provide feedback or report issues, contact [Logz.io support team](mailto:help@logz.io). Your feedback helps us improve the AI Agent experience.