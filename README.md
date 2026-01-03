# AI-QQ-Bot Infrastructure (n8n & NapCat)

<div align="center">

An intelligent automation framework for QQ interaction, integrating **n8n** for orchestration and **NapCat** for protocol handling.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](./LICENSE)
[![n8n](https://img.shields.io/badge/n8n-Workflow-orange?style=for-the-badge&logo=n8n)](https://n8n.io/)
[![Docker](https://img.shields.io/badge/Docker-Compose-blue?style=for-the-badge&logo=docker)](https://www.docker.com/)

[**English**](./README.md) | [**简体中文**](./docs/guides/README_CN.md)

</div>

---

## 🏗️ System Architecture

> **User Guide**: GitHub's native viewer supports high-resolution **zooming** and **dragging**. Click the diagrams below to enter the full-screen interactive mode.

### System Infrastructure

<a href="./docs/architecture/system_infrastructure_solid.png">
  <img src="./docs/architecture/system_infrastructure_solid.png" width="100%" alt="System Infrastructure">
</a>

### Logical Flow

<a href="./docs/architecture/logical_functional_flow_solid.png">
  <img src="./docs/architecture/logical_functional_flow_solid.png" width="100%" alt="Logical Flow">
</a>

### Database Schema

<a href="./docs/architecture/database_schema_relationship_solid.png">
  <img src="./docs/architecture/database_schema_relationship_solid.png" width="100%" alt="Database Schema">
</a>

---


## 📊 Workflow Showcase

### [Workflow Overview](./docs/workflows/QQBot_Workflows_Overview.png)

<a href="./docs/workflows/QQBot_Workflows_Overview.png">
<img src="./docs/workflows/QQBot_Workflows_Overview_Partial.png" width="100%" alt="Workflow Overview">
</a>

### Workflow Navigation

The **Main Handler** is the primary entry point for all incoming QQ messages. All sub-workflows and tools are organized in the collapsible gallery below.

#### [Main Handler](./docs/workflows/QQBot_MainHandler.png)

<a href="./docs/workflows/QQBot_MainHandler.png">
<img src="./docs/workflows/QQBot_MainHandler.png" width="100%" alt="Main Handler">
</a>

<details>
<summary><b>📂 Click to expand Full Module Gallery (Sub-flows & AI Tools)</b></summary>

> ### 🧩 Category: Message Processing (Sub-workflows)
> 
> 
> ##### [Emoji Resolve](./docs/workflows/QQBot_Sub_EmojiResolve.png)
> 
> 
> <a href="./docs/workflows/QQBot_Sub_EmojiResolve.png">
> <img src="./docs/workflows/QQBot_Sub_EmojiResolve.png" width="100%">
> </a>
>
> ##### [Media Analysis](./docs/workflows/QQBot_Sub_MediaAnalysis.png)
> 
> <a href="./docs/workflows/QQBot_Sub_MediaAnalysis.png">
> <img src="./docs/workflows/QQBot_Sub_MediaAnalysis.png" width="100%">
> </a>
>
> ##### [At Message Resolve](./docs/workflows/QQBot_Sub_AtMessageResolve.png)
> 
> 
> <a href="./docs/workflows/QQBot_Sub_AtMessageResolve.png">
> <img src="./docs/workflows/QQBot_Sub_AtMessageResolve.png" width="100%">
> </a>
>
> ##### [Recent Summary](./docs/workflows/QQBot_Sub_RecentSummary.png)
> 
> 
> <a href="./docs/workflows/QQBot_Sub_RecentSummary.png">
> <img src="./docs/workflows/QQBot_Sub_RecentSummary.png" width="100%">
> </a>
>
> ##### [Embedding Service](./docs/workflows/QQBot_Sub_Embedding.png)
> 
> 
> <a href="./docs/workflows/QQBot_Sub_Embedding.png">
> <img src="./docs/workflows/QQBot_Sub_Embedding.png" width="100%">
> </a>

> ---

> ### 🔧 Category: AI Agent Tools
> 
> ##### [History Context Tool](./docs/workflows/QQBot_Tool_HistoryContext.png)
> 
> <a href="./docs/workflows/QQBot_Tool_HistoryContext.png">
> <img src="./docs/workflows/QQBot_Tool_HistoryContext.png" width="100%">
> </a>
>
> ##### [History Search Tool](./docs/workflows/QQBot_Tool_HistorySearch.png)
> 
> <a href="./docs/workflows/QQBot_Tool_HistorySearch.png">
> <img src="./docs/workflows/QQBot_Tool_HistorySearch.png" width="100%">
> </a>
>
> ##### [Web Search Tool](./docs/workflows/QQBot_Tool_WebSearch.png)
> 
> 
> <a href="./docs/workflows/QQBot_Tool_WebSearch.png">
> <img src="./docs/workflows/QQBot_Tool_WebSearch.png" width="100%">
> </a>
>
> ##### [Game Deals Tool](./docs/workflows/QQBot_Tool_GameDeals.png)
> 
> 
> <a href="./docs/workflows/QQBot_Tool_GameDeals.png">
> <img src="./docs/workflows/QQBot_Tool_GameDeals.png" width="100%">
> </a>

> ---

> ### ⚙️ Category: System Services
> 
> 
> ##### [Service Status Monitor](./docs/workflows/QQBot_Service_StatusMonitor.png)
> 
> 
> <a href="./docs/workflows/QQBot_Service_StatusMonitor.png">
> <img src="./docs/workflows/QQBot_Service_StatusMonitor.png" width="60%">
> </a>
>
> ##### [Bark Notifier Service](./docs/workflows/Global_Service_BarkNotifier.png)
> 
> 
> <a href="./docs/workflows/Global_Service_BarkNotifier.png">
> <img src="./docs/workflows/Global_Service_BarkNotifier.png" width="40%">
> </a>

</details>

---

## 🚀 Deployment & Setup Guide

This guide details the steps to deploy the n8n and napcat services and configure them to work together.

### 1. Initial Environment Setup

Before launching the containers, you need to configure the environment and set up the shared Docker network.

1.  **Configure Environment Files:**
    *   Edit [`deploy/n8n-compose/.env`](./deploy/n8n-compose/.env) and [`deploy/napcat-compose/.env`](./deploy/napcat-compose/.env) to match your local setup (e.g., set your domain for `N8N_HOST`, user/group IDs for `NAPCAT_UID`/`NAPCAT_GID`, etc.).

2.  **Create Docker Network:**
    The services communicate over a shared Docker network. Create it with the following command, using the network name defined in your `.env` files:
    ```bash
    docker network create napcat-n8n-network
    ```

### 2. Deploying Containers

With the environment configured, launch the services using Docker Compose. It's recommended to start the `n8n` stack first.

1.  **Start n8n Service:**
    ```bash
    cd deploy/n8n-compose
    docker compose up -d --build
    ```

2.  **Start napcat Service:**
    ```bash
    cd deploy/napcat-compose
    docker compose up -d --build
    ```

### 3. Accessing Services & Logging In

1.  **n8n Web UI:**
    *   Access n8n through the domain you configured in [`deploy/n8n-compose/.env`](./deploy/n8n-compose/.env) for the `N8N_HOST` variable (e.g., `http://your.domain.com`).

2.  **napcat Web UI:**
    *   Access the napcat web interface via your server's IP and the `NAPCAT_WEB_PORT` from its [`.env`](./deploy/napcat-compose/.env) file. For example: `http://192.168.1.100:6099/webui/`.

3.  **napcat QQ Login:**
    You need to log in to QQ by scanning a QR code. You can get this code in two ways:
    *   **Method 1 (Command Line):** View the container logs to get a QR code image link. The container name is defined in [`deploy/napcat-compose/.env`](./deploy/napcat-compose/.env).
        ```bash
        docker logs napcat
        ```
    *   **Method 2 (Web UI):** In the napcat web interface, navigate to "猫猫日志" -> "历史日志" to find the QR code.
    *   Use your mobile QQ app to scan the QR code and complete the login.

### 4. Application & Workflow Configuration

This step prepares the configuration before importing workflows into n8n.

1.  **Modify Workflow Placeholders:**
    *   Edit the `SENSITIVE_MAP` dictionary in [`scripts/workflow_configurator.py`](./scripts/workflow_configurator.py), specifically the `# Infrastructure & Tokens` section, to match your environment's real values (e.g., your actual Bark token, API keys, etc.).

2.  **Run the Configurator Script:**
    This script will replace the placeholders in the local workflow files with the real values you just set in `SENSITIVE_MAP`.
    ```bash
    python scripts/workflow_configurator.py
    ```

### 5. Final n8n Setup

After preparing the workflows, import them and set up the necessary credentials inside n8n.

1.  **Import Workflows to n8n:**
    *   Navigate to your n8n web UI.
    *   Manually import the now-configured JSON files from the [`n8n/workflows/`](./n8n/workflows/) directory.

2.  **Configure Credentials in n8n UI:**
    After importing, your workflows will not run correctly until you configure the credentials for the services they use. In the n8n UI, find the corresponding nodes and create/select the credentials for:
    *   **NapCat Token:** The private token you will create in the napcat HTTP Server (see next step).
    *   **LLM APIs:** API keys for services like DeepSeek, Qwen, etc.
    *   **Search APIs:** Credentials for services like Aliyun Search.

### 6. Final napcat Setup

Finally, configure napcat to communicate with n8n.

1.  **napcat Connection Configuration:**
    Log in to the napcat web UI and navigate to the "网络配置" section.
    *   **Create an "HTTP 服务器" (HTTP Server):**
        *   **Host:** `0.0.0.0`
        *   **Port:** `3000` (This corresponds to the host and port in `REDACTED_NAPCAT_HOST` within [`scripts/workflow_configurator.py`](./scripts/workflow_configurator.py)).
        *   **消息格式 (Message Format):** `Array`
        *   **Token:** Create a secure, private token. This same token must be used in the n8n credential for NapCat (see step 5.2).
    *   **Create an "HTTP 客户端" (HTTP Client):**
        *   **URL:** `http://n8n:5678/webhook/napcat-webhook` (This URL corresponds to `REDACTED_NAPCAT_WEBHOOK_NAME` in [`scripts/workflow_configurator.py`](./scripts/workflow_configurator.py)).
        *   **上报自身消息 (Report Self Messages):** `True`
        *   **Token:** Leave this blank. For added security, you can set a token here and add an `IF` node after the `NapCatTriger` webhook node in your n8n workflow to manually check for a matching `Bearer` header.


---

## 🛠️ Maintenance & Scripts

* **[workflow_configurator.py](./scripts/workflow_configurator.py)**: A Python utility to replace placeholders in workflow files with your actual private values before importing them into n8n.
* **[backup_to_samba_template.sh](./scripts/backup_to_samba_template.sh)**: A template script to automate backing up the entire project (n8n data, Postgres database, and compose files) to a remote Samba share.

---

## 📂 Repository Structure

```text
ai-qq-bot-n8n/
├── deploy/               # Docker Compose deployment stacks
│   ├── n8n-compose/      # n8n, Traefik, and Postgres stack
│   │   ├── compose.yaml
│   │   ├── .env.template
│   │   └── .env
│   └── napcat-compose/   # napcat stack
│       ├── docker-compose.yml
│       ├── .env.template
│       └── .env
├── n8n/
│   └── workflows/        # Redacted n8n workflow JSON files
├── scripts/              # Project maintenance tools
│   ├── backup_to_samba_template.sh
│   └── workflow_configurator.py
└── README.md
```

---

## 🙏 Acknowledgements & Resources

This project is built upon and integrates with several fantastic open-source projects and services.

| Project / Service | Category | Link & Purpose |
| :--- | :--- | :--- |
| n8n | Core Framework | [![n8n Docs](https://img.shields.io/badge/n8n-Docs-orange?logo=n8n)](https://docs.n8n.io/hosting/installation/docker/) |
| NapCat | Core Framework | [![NapCat Repo](https://img.shields.io/badge/GitHub-Repo-blue?logo=github)](https://github.com/NapNeko/NapCat.Docker.Framework) |
| Oray PeanutShell | Deployment & Services | [![PeanutShell Website](https://img.shields.io/badge/花生壳-Website-brightgreen)](https://hsk.oray.com/) |
| IsThereAnyDeal | Deployment & Services | [![ITAD API](https://img.shields.io/badge/ITAD-API-blueviolet)](https://isthereanydeal.com/apps/) |
| DeepSeek | AI API | [![DeepSeek API](https://img.shields.io/badge/DeepSeek-API_Keys-informational)](https://platform.deepseek.com/api_keys) |
| Aliyun Bailian | AI API | [![Aliyun Bailian](https://img.shields.io/badge/阿里云百炼-API_Keys-orangered?logo=alibabacloud)](https://bailian.console.aliyun.com/tab=model#/api-key) |
| OpenAI API | AI API (Alternative) | [![OpenAI API](https://img.shields.io/badge/OpenAI-API-black?logo=openai)](https://openai.com/index/openai-api/) |
| Aliyun OpenSearch | Search API | [![Aliyun OpenSearch](https://img.shields.io/badge/阿里云开放搜索-API_Keys-orangered?logo=alibabacloud)](https://opensearch.console.aliyun.com/cn-shanghai/rag/api-key) |
| Google Search API | Search API (Alternative) | [![Google Search API](https://img.shields.io/badge/Google-API-4285F4?logo=google)](https://console.cloud.google.com/apis/dashboard) |
