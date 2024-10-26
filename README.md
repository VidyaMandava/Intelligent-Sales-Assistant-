# Intelligent-Sales-Assistant 🚀-

This project demonstrates an intelligent solution for assigning high-performing agents to healthcare providers (HCPs) based on a composite score model and advanced language model (LLM) insights, ensuring efficient, personalized interactions. Through data-driven and AI-enhanced insights, this solution optimizes agent-HCP alignment to drive better engagement and sales outcomes.

**Introduction**
In the healthcare and pharmaceutical industry, aligning the right sales agents with HCPs is crucial for improving engagement and sales performance. This project addresses this need through a composite score model that selects the best-fit agents for each HCP by factoring in agent performance, geographic proximity, and therapeutic focus. The composite score method, combined with AI-generated insights, enables sales agents to receive personalized, actionable information about their assigned HCPs, promoting more efficient and meaningful interactions.

**Problem Statement**
The objective is to optimize agent-HCP assignments to improve engagement efficiency, ensuring that high-performance agents are assigned to HCPs nearby and align with HCP needs. By leveraging a composite score model and LLM-generated insights, agents gain contextually relevant summaries and actionable suggestions based on historical interactions, ultimately enhancing HCP engagement.

**Solution Approach**
Data Analysis: Analyze historical agent and HCP data to identify relevant features such as Performance_Rating, Distance, and Therapeutic_Focus.

**Composite Score Calculation:**
Compute a composite score using factors like agent performance, proximity, and product alignment.
Rank agents for each HCP based on the composite score to select the best-fit agent.

**Large Language Model (LLM) Integration:**
Use an LLM to generate personalized, contextual summaries for agents on their assigned HCPs.
Provide actionable insights derived from historical data and patterns.

**Agent Application Interface:**
The LLM-generated summaries are displayed on an agent-facing application interface, allowing agents to access enhanced, insightful information for each assigned HCP.

*Technical Details*
Datasets
Agent Data: Includes agent performance ratings, geographic location, and therapeutic focus.
HCP Data: Consists of HCP location, specialty, and preferred drug information.
Prescription data: Consists drug prescriptions & frequency
Interactions data: Historic interactions with HCP, outcome, notes, drug presented.

*Techniques Used*
Composite Score Model: Calculates an agent’s score for each HCP based on weighted criteria.
Distance Calculation: Implements the Haversine formula to determine proximity between agents and HCPs.
Large Language Model (LLM): Utilizes an mixtral-8x7b-instruct LLM to generate contextual summaries and insights, powered by Retrieval-Augmented Generation (RAG) to draw on both real-time and historical data.
Model Flow
Data Preparation: Cleans and preprocesses agent and HCP data.
Score Calculation: Calculates composite scores by combining scaled values of Performance_Rating, Distance, and Product_Alignment.
LLM Insight Generation: LLM provides summaries for assigned HCPs, enriching raw data with actionable recommendations.
User Interface: Shows LLM insights and assigned HCP details to agents.

Project Structure

intelligent-sales-agent/
├── 1_Datasets_Generation/                   # Data files used in the project
├── app.py                  # Main application script
├── 2_Intelligent_HCP_Assignment/                  # Composite score model and ML pipeline scripts
├── 3_Personalized_Briefing_Pack/                    # Scripts for integrating and generating LLM-based summaries
├── README.md               # Project documentation
└── results/                # Results and outputs of the model
Setup and Installation
Clone the Repository

bash
Copy code
git clone https://github.com/yourusername/intelligent-sales-agent.git
cd intelligent-sales-agent
Install Requirements

bash
Copy code
pip install -r requirements.txt
Set Up Databricks CLI for Deployment

Ensure you have a valid access token and configure Databricks CLI:
bash
Copy code
databricks configure --token
Usage
Load agent and HCP data, and run the composite score calculation model to assign agents.
Generate LLM Summaries

Run the llm scripts to generate contextual insights for each agent's assigned HCPs.
Deploy and Access Application

Use Databricks CLI to deploy the app and sync your workspace:
bash
Copy code
databricks workspace import_dir . /path/to/your-workspace
Agents can then log in to view their assigned HCPs with LLM-generated insights.
Results
The Intelligent Sales Agent Assignment project has shown improved agent-HCP alignment by:

Prioritizing agents with higher performance and closer proximity.
Providing actionable insights and tailored information for each agent, leading to increased engagement efficiency.
Future Enhancements
Dynamic Weight Adjustment: Allow weight factors in the composite score calculation to be adjusted based on feedback and performance metrics.
Extended LLM Insights: Integrate additional context from recent market trends and specific HCP preferences.
Real-Time Monitoring: Add real-time updates on agent assignments and HCP interactions to improve responsiveness.
License
This project is licensed under the MIT License.
