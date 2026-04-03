from django.shortcuts import render
from django.http import Http404

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def experience(request):
    return render(request, 'portfolio/experience.html')

def skills(request):
    return render(request, 'portfolio/skills.html')

def certifications(request):
    return render(request, 'portfolio/certifications.html')

def contact(request):
    return render(request, 'portfolio/contact.html')

def projects(request):
    return render(request, 'portfolio/projects.html', {'projects': PROJECTS})

def project_detail(request, slug):
    project = PROJECTS.get(slug)
    if not project:
        raise Http404
    return render(request, 'portfolio/project_detail.html', {'project': project, 'slug': slug})


PROJECTS = {

    'aws-bgp-optimization': {
        'title': 'AWS Hybrid Network – BGP Optimization',
        'category': 'AWS Networking',
        'status': 'Completed',
        'tags': ['AWS', 'BGP', 'Direct Connect', 'Transit Gateway', 'VPC'],
        'image': 'portfolio/img/aws-architecture.png',
        'summary': 'Resolved routing asymmetry between Direct Connect and VPN by implementing BGP community tagging to control Local Preference in AWS Transit Gateway.',
        'problem': 'Return traffic was using VPN instead of Direct Connect because Local Preference was higher on VPN than on DX Gateway. AS_PATH prepend (65512 65512) was never evaluated — LP decided first.',
        'solution': 'Applied BGP Community Tags on Transit VIFs. DX Transit VIFs → 7224:7300 (High preference). VPN connections → 7224:7100 (Low preference).',
        'impact': 'Traffic now correctly prefers Direct Connect over VPN, reducing latency and costs across multi-region deployments (us-east-1 and eu-central-1).',
        'tech': ['AWS Transit Gateway', 'Direct Connect', 'BGP Communities', 'VPC Inspection', 'Network Firewall', 'AS_PATH Prepend'],
        'sections': [
            {
                'icon': '🎯',
                'label': 'Summary',
                'type': 'summary',
                'content': 'Resolved routing asymmetry between Direct Connect and VPN by implementing BGP community tagging to control Local Preference in AWS Transit Gateway across a multi-region enterprise hybrid network.'
            },
            {
                'icon': '⚠',
                'label': 'Problem',
                'type': 'problem',
                'content': 'Return traffic was using VPN instead of Direct Connect because Local Preference was higher on VPN than on DX Gateway. AS_PATH prepend (65512 65512) was never evaluated — LP decided first, causing asymmetric routing and increased latency.'
            },
            {
                'icon': '✓',
                'label': 'Solution',
                'type': 'solution',
                'content': 'Applied BGP Community Tags on Transit VIFs. DX Transit VIFs → 7224:7300 (High preference). VPN connections → 7224:7100 (Low preference). This forces correct path selection without modifying AS_PATH.'
            },
            {
                'icon': '📈',
                'label': 'Impact',
                'type': 'impact',
                'content': 'Traffic now correctly prefers Direct Connect over VPN, reducing latency by ~40ms per round-trip and eliminating unnecessary VPN data transfer costs across multi-region deployments.'
            },
        ]
    },

    'aws-3tier-ha': {
        'title': '3-Tier App — High Availability on AWS',
        'category': 'AWS Architecture',
        'status': 'Completed',
        'tags': ['ECS Fargate', 'RDS Aurora', 'ElastiCache', 'ALB', 'CloudFront', 'WAF'],
        'image': 'portfolio/img/aws-3tier-ha.png',
        'summary': 'Designed a highly available 3-tier web architecture solving session persistence at scale using ElastiCache Redis, with zero-downtime auto scaling and enterprise-grade security at the edge.',
        'problem': (
            'A growing e-commerce platform was experiencing critical session loss during Auto Scaling events. '
            'When instances were replaced, users were logged out mid-session. '
            'The initial approach of storing sessions in cookies had two fatal flaws: '
            '(1) cookies have a 4KB size limit — insufficient for rich session data, '
            'and (2) sensitive session data exposed client-side violates security best practices. '
            'The platform needed to scale from 1,000 to 50,000 concurrent users without any session disruption.'
        ),
        'solution': (
            'Implemented a 3-tier architecture with session state externalized to ElastiCache Redis Cluster Mode. '
            'All ECS Fargate containers read/write session data from a centralized Redis cluster — '
            'when Auto Scaling replaces an instance, the new container retrieves the session seamlessly. '
            'VPC Endpoints for ECR and S3 keep container pulls and asset fetches private. '
            'CloudFront + WAF handles edge caching and DDoS protection. '
            'RDS Aurora Multi-AZ ensures database resilience with automatic failover in under 30 seconds.'
        ),
        'impact': (
            'Zero session drops during Auto Scaling events. '
            'Application scales elastically from 1K to 50K concurrent users. '
            'Database failover reduced from ~2min (RDS single-AZ) to <30s (Aurora Multi-AZ). '
            'WAF blocked 98% of malicious requests at the edge before reaching the app tier. '
            'Infrastructure cost optimized by 35% using Fargate Spot for non-critical workloads.'
        ),
        'tech': ['ECS Fargate', 'ALB', 'ElastiCache Redis', 'RDS Aurora Multi-AZ', 'CloudFront', 'WAF', 'VPC Endpoints', 'ECR', 'Secrets Manager', 'Auto Scaling'],
        'sections': [
            {
                'icon': '🎯',
                'label': 'Summary',
                'type': 'summary',
                'content': 'Designed a highly available 3-tier web architecture solving session persistence at scale using ElastiCache Redis, with zero-downtime auto scaling and enterprise-grade security at the edge.'
            },
            {
                'icon': '⚠',
                'label': 'Problem — Session Loss at Scale',
                'type': 'problem',
                'content': 'A growing e-commerce platform experienced critical session loss during Auto Scaling events. When instances were replaced, users were logged out mid-session. Cookies failed: 4KB size limit was insufficient for rich session data, and exposing sensitive data client-side violated security requirements. The platform needed to scale from 1,000 to 50,000 concurrent users without disruption.'
            },
            {
                'icon': '✓',
                'label': 'Solution — Externalized Session State',
                'type': 'solution',
                'content': 'Externalized session state to ElastiCache Redis Cluster Mode. All ECS Fargate containers read/write from a centralized Redis cluster — when Auto Scaling replaces an instance, the new container retrieves the session seamlessly. VPC Endpoints keep traffic private. CloudFront + WAF handles edge protection. RDS Aurora Multi-AZ provides automatic database failover in under 30 seconds.'
            },
            {
                'icon': '📈',
                'label': 'Impact — Zero Session Drops',
                'type': 'impact',
                'content': 'Zero session drops during Auto Scaling events. Application scales elastically from 1K to 50K concurrent users. Database failover reduced from ~2min to <30s. WAF blocked 98% of malicious requests at the edge. Infrastructure cost optimized by 35% using Fargate Spot for non-critical workloads.'
            },
        ],
        'architecture_notes': [
            'Sessions stored in Redis with TTL — no sticky sessions required on ALB',
            'VPC Endpoints eliminate internet egress for ECR/S3 — security + cost saving',
            'Secrets Manager rotates DB credentials automatically — zero hardcoded secrets',
            'CloudFront caches static assets globally — app tier only handles dynamic requests',
        ]
    },

    'aws-serverless': {
        'title': 'Serverless Real-Time Event Processing',
        'category': 'Serverless Architecture',
        'status': 'Completed',
        'tags': ['API Gateway', 'Lambda', 'DynamoDB', 'SQS', 'SNS', 'CloudFront', 'Cognito'],
        'image': 'portfolio/img/aws-serverless.png',
        'summary': 'Built a fully serverless backend capable of handling 100,000+ concurrent events per second using API Gateway, Lambda, and DynamoDB — with zero server management and automatic scaling to zero.',
        'problem': (
            'A logistics company needed to process real-time GPS tracking events from 80,000+ vehicle sensors '
            'simultaneously. Their existing EC2-based backend could not handle traffic spikes during peak hours '
            '(deliveries 8AM–2PM) and sat idle at 5% utilization overnight — paying full price 24/7. '
            'Cold start latency on their monolithic API was causing 3–8 second delays in event acknowledgment. '
            'Additionally, failed events were being silently dropped with no retry mechanism.'
        ),
        'solution': (
            'Replaced the monolithic API with an event-driven serverless architecture. '
            'API Gateway receives sensor events and validates JWT tokens via Cognito — no servers needed. '
            'Lambda functions (512MB, provisioned concurrency for hot paths) process events in parallel. '
            'DynamoDB with a VPC Gateway Endpoint stores telemetry with on-demand capacity mode — '
            'scales from 0 to 1M writes/second automatically. '
            'SQS queues decouple event ingestion from processing — failed events retry 3x before going to DLQ. '
            'SNS fan-out delivers processed events to downstream consumers (analytics, alerts, dashboards). '
            'S3 + CloudFront serves the React frontend globally with <50ms TTFB.'
        ),
        'impact': (
            'System handles 100K concurrent events/second during peak — previously maxed at 8K. '
            'Zero dropped events — SQS DLQ captures and alerts on all failures. '
            'Infrastructure cost reduced by 72% — pay only for actual invocations, not idle EC2. '
            'Cold start eliminated for critical paths using provisioned concurrency. '
            'Deployment time reduced from 45 minutes (EC2 + AMI) to 90 seconds (Lambda deploy).'
        ),
        'tech': ['API Gateway', 'Lambda', 'DynamoDB', 'SQS + DLQ', 'SNS', 'CloudFront', 'S3', 'Cognito', 'VPC Gateway Endpoint', 'EventBridge'],
        'sections': [
            {
                'icon': '🎯',
                'label': 'Summary',
                'type': 'summary',
                'content': 'Built a fully serverless backend handling 100,000+ concurrent events/second from IoT vehicle sensors — with zero server management, automatic scaling, and 72% cost reduction vs the previous EC2 architecture.'
            },
            {
                'icon': '⚠',
                'label': 'Problem — Unpredictable Traffic Spikes',
                'type': 'problem',
                'content': 'A logistics company needed to process real-time GPS events from 80,000+ vehicle sensors simultaneously. Their EC2 backend maxed at 8K concurrent events and sat idle at 5% utilization overnight — paying full price 24/7. Failed events were silently dropped with no retry mechanism, causing data loss.'
            },
            {
                'icon': '✓',
                'label': 'Solution — Event-Driven Serverless',
                'type': 'solution',
                'content': 'API Gateway validates JWT via Cognito and routes to Lambda functions with provisioned concurrency for hot paths. DynamoDB with VPC Gateway Endpoint scales to 1M writes/second on-demand. SQS decouples ingestion from processing — failed events retry 3x before DLQ. SNS fan-out distributes to downstream consumers. S3 + CloudFront serves frontend globally.'
            },
            {
                'icon': '📈',
                'label': 'Impact — 12x Throughput, 72% Cost Reduction',
                'type': 'impact',
                'content': 'System handles 100K concurrent events/second vs previous 8K. Zero dropped events — SQS DLQ captures all failures. Infrastructure cost reduced 72% — pay per invocation not idle EC2. Deployment time: 45 min → 90 seconds. Cold starts eliminated for critical paths via provisioned concurrency.'
            },
        ],
        'architecture_notes': [
            'DLQ (Dead Letter Queue) on SQS — every failed event is captured, never silently dropped',
            'Provisioned concurrency on Lambda eliminates cold starts for latency-sensitive paths',
            'DynamoDB on-demand mode — no capacity planning, scales automatically with traffic',
            'VPC Gateway Endpoint for DynamoDB — zero cost, zero internet exposure for DB traffic',
        ]
    },

    'aws-disaster-recovery': {
        'title': 'Multi-Region Disaster Recovery on AWS',
        'category': 'Disaster Recovery',
        'status': 'Completed',
        'tags': ['Route 53', 'Aurora Global', 'EKS', 'S3 CRR', 'Pilot Light', 'RTO', 'RPO'],
        'image': 'portfolio/img/aws-disaster-recovery.png',
        'summary': 'Architected a multi-region DR strategy achieving RTO < 15 min and RPO < 1 min using Aurora Global Database, EKS pilot light, and automated Route 53 failover — at 60% lower cost than a full active-active setup.',
        'problem': (
            'A financial services company processing $2M/hour in transactions had a single-region deployment in us-east-1. '
            'A 4-hour outage in 2023 caused $8M in lost transactions and regulatory penalties. '
            'Their SLA mandated: RTO < 15 minutes, RPO < 1 minute. '
            'A full active-active multi-region setup was quoted at $180K/month — 3x their current infrastructure budget. '
            'They needed enterprise-grade resilience without enterprise-grade costs.'
        ),
        'solution': (
            'Implemented a Pilot Light DR strategy with eu-west-1 as standby. '
            'Aurora Global Database replicates data to eu-west-1 with ~1 second lag — meeting RPO < 1 min. '
            'EKS cluster in eu-west-1 runs at minimal scale (2 nodes) — "pilot light" kept warm but not serving traffic. '
            'Route 53 health checks monitor the primary ALB every 10 seconds. '
            'On failure detection, Route 53 DNS TTL (60s) switches traffic to eu-west-1 automatically. '
            'EKS Auto Scaling triggers scale-up to full capacity within 8 minutes. '
            'Aurora Global promotes the eu-west-1 replica to writer in under 1 minute. '
            'S3 Cross-Region Replication keeps all static assets and backups synchronized. '
            'Total failover time: ~12 minutes — well within the 15-minute RTO.'
        ),
        'impact': (
            'RTO achieved: 12 minutes (SLA requires < 15 min). '
            'RPO achieved: < 1 minute (Aurora Global replication lag ~1s). '
            'DR infrastructure cost: $42K/month vs $180K for active-active — 77% savings. '
            'First DR drill completed in 11 minutes with zero data loss. '
            'Regulatory compliance: meets financial services DR requirements (SOC2, PCI-DSS). '
            'Confidence: executives can now trigger failover from a single Route 53 policy change.'
        ),
        'tech': ['Route 53 Health Checks', 'Aurora Global Database', 'EKS (Pilot Light)', 'S3 Cross-Region Replication', 'CloudWatch Alarms', 'ALB', 'Auto Scaling', 'Systems Manager'],
        'sections': [
            {
                'icon': '🎯',
                'label': 'Summary',
                'type': 'summary',
                'content': 'Architected a multi-region Pilot Light DR strategy achieving RTO < 15 min and RPO < 1 min for a financial services platform processing $2M/hour — at 77% lower cost than active-active alternatives.'
            },
            {
                'icon': '⚠',
                'label': 'Problem — $8M Outage Risk',
                'type': 'problem',
                'content': 'A financial services company had a single-region deployment in us-east-1. A 4-hour outage caused $8M in lost transactions. SLA mandated RTO < 15 min, RPO < 1 min. Full active-active multi-region was quoted at $180K/month — 3x their budget. They needed enterprise resilience without enterprise costs.'
            },
            {
                'icon': '✓',
                'label': 'Solution — Pilot Light Strategy',
                'type': 'solution',
                'content': 'Aurora Global Database replicates to eu-west-1 with ~1s lag (RPO met). EKS pilot light in eu-west-1 runs at 2 nodes — warm but not serving traffic. Route 53 health checks every 10s trigger DNS failover (TTL 60s). EKS scales to full capacity in 8 min. Aurora promotes replica to writer in <1 min. Total failover: ~12 min.'
            },
            {
                'icon': '📈',
                'label': 'Impact — 77% Cost Savings',
                'type': 'impact',
                'content': 'RTO: 12 min (SLA < 15 min ✓). RPO: <1 min (Aurora lag ~1s ✓). Cost: $42K/month vs $180K active-active — 77% savings. First drill: 11 min, zero data loss. Meets SOC2 and PCI-DSS DR requirements. Executives can trigger failover from a single Route 53 policy change.'
            },
        ],
        'architecture_notes': [
            'Pilot Light vs Warm Standby: pilot light = minimal compute running, scale up on failover',
            'Aurora Global promotes replica in <1 min — no manual intervention needed',
            'Route 53 TTL set to 60s — DNS propagation is the bottleneck, not AWS infrastructure',
            'S3 CRR (Cross-Region Replication) runs continuously — assets always in sync',
        ]
    },

    'aws-security-governance': {
        'title': 'AWS Security & Governance Architecture',
        'category': 'Security & Compliance',
        'status': 'Completed',
        'tags': ['AWS Organizations', 'IAM Identity Center', 'GuardDuty', 'Security Hub', 'CloudTrail', 'Config', 'Macie'],
        'image': 'portfolio/img/aws-security-governance.png',
        'summary': 'Designed an enterprise-grade security and governance framework for a 12-account AWS Organization — centralizing identity, automating compliance enforcement, and achieving continuous threat detection with automated remediation.',
        'problem': (
            'A healthcare company (HIPAA regulated) operating across 12 AWS accounts had no centralized visibility. '
            'Each team managed their own IAM users — 340 individual IAM users with no MFA enforcement. '
            'S3 buckets with PHI (Protected Health Information) were publicly accessible in 3 accounts. '
            'There was no audit trail — CloudTrail was disabled in 4 accounts. '
            'A security assessment found 47 critical findings. '
            'The company faced potential HIPAA fines of up to $1.9M per violation category.'
        ),
        'solution': (
            'Deployed AWS Control Tower to establish a governed multi-account landing zone. '
            'IAM Identity Center (SSO) replaced 340 individual IAM users — single identity source, MFA enforced. '
            'Service Control Policies (SCPs) at the OU level: block public S3, enforce CloudTrail, deny root usage. '
            'AWS Config rules automatically detect and remediate non-compliant resources (auto-remediation via SSM). '
            'GuardDuty enabled across all 12 accounts with delegated admin in the security account. '
            'Macie scans S3 buckets continuously for PHI/PII exposure. '
            'Security Hub aggregates findings from GuardDuty, Macie, Config, and Inspector into a single dashboard. '
            'EventBridge routes critical findings to Lambda for auto-remediation (e.g., revoke public S3 access instantly). '
            'CloudTrail Organization Trail captures all API calls across all accounts into a centralized S3 bucket with Athena for analysis.'
        ),
        'impact': (
            'Zero IAM users — 340 replaced by SSO with MFA. '
            '47 critical findings reduced to 0 within 72 hours of deployment. '
            'All public S3 buckets automatically blocked via SCP — PHI exposure eliminated. '
            'CloudTrail enabled across all 12 accounts — full audit trail for HIPAA compliance. '
            'Mean time to detect (MTTD): 8 hours → 4 minutes (GuardDuty real-time alerts). '
            'Mean time to remediate (MTTR): 3 days → 8 minutes (automated Lambda remediation). '
            'HIPAA audit passed with zero findings — potential $1.9M fine avoided.'
        ),
        'tech': ['AWS Control Tower', 'IAM Identity Center', 'SCPs', 'GuardDuty', 'Macie', 'Security Hub', 'AWS Config', 'CloudTrail', 'EventBridge', 'Lambda', 'Athena', 'Inspector'],
        'sections': [
            {
                'icon': '🎯',
                'label': 'Summary',
                'type': 'summary',
                'content': 'Designed an enterprise security framework for a 12-account HIPAA-regulated AWS Organization — eliminating 340 IAM users, automating compliance enforcement, and reducing threat detection time from 8 hours to 4 minutes.'
            },
            {
                'icon': '⚠',
                'label': 'Problem — HIPAA Risk Across 12 Accounts',
                'type': 'problem',
                'content': 'A healthcare company had 340 individual IAM users with no MFA, PHI-containing S3 buckets publicly accessible in 3 accounts, CloudTrail disabled in 4 accounts, and 47 critical security findings. Facing potential HIPAA fines up to $1.9M per violation category.'
            },
            {
                'icon': '✓',
                'label': 'Solution — Zero-Trust Governance',
                'type': 'solution',
                'content': 'Control Tower establishes governed landing zone. IAM Identity Center replaces all IAM users with SSO + MFA. SCPs block public S3, enforce CloudTrail, deny root. Config auto-remediates non-compliant resources via SSM. GuardDuty + Macie + Inspector feed into Security Hub. EventBridge routes findings to Lambda for instant remediation. Organization CloudTrail → S3 → Athena for forensic analysis.'
            },
            {
                'icon': '📈',
                'label': 'Impact — HIPAA Audit Passed',
                'type': 'impact',
                'content': 'Zero IAM users — 340 replaced by SSO with MFA. 47 critical findings → 0 in 72 hours. All PHI exposure eliminated via SCPs. MTTD: 8h → 4 min. MTTR: 3 days → 8 min. Full HIPAA audit passed with zero findings. $1.9M potential fine avoided.'
            },
        ],
        'architecture_notes': [
            'SCPs are guardrails — they override even admin permissions at account level',
            'Security Hub aggregates findings from 6 services — single pane of glass for CISO',
            'Auto-remediation via Lambda: public S3 bucket detected → access blocked in <30 seconds',
            'Organization CloudTrail cannot be disabled by member accounts — SCP enforced',
        ]
    },

    'containerized-portfolio': {
        'title': 'Technical Portfolio — Django & Render Deploy',
        'category': 'Docker & DevOps',
        'status': 'Completed',
        'tags': ['Django', 'Python', 'HTML/CSS', 'WhiteNoise', 'Gunicorn', 'Render'],
        'image': '',
        'summary': 'Full-stack technical portfolio built with Django, pure CSS and HTML — without frontend frameworks. Developed through Practical Engineering with AI: using generative AI as a productivity copilot to materialize a technical vision, not as a replacement for engineering judgment.',
        'problem': (
            'A static PDF resume cannot demonstrate the depth of an infrastructure engineer\'s work. '
            'Recruiters and hiring managers need to see real architecture decisions, not bullet points. '
            'The challenge: build a professional, dynamic portfolio without frontend development expertise, '
            'while keeping full control over the technical content and deployment.'
        ),
        'solution': (
            'Built on a Django base from the Python course, extended into a full portfolio system. '
            'Practical Engineering with AI was used as the development methodology: '
            'AI assisted with HTML/CSS structure and Django wiring, while all technical content — '
            'AWS architectures, BGP configurations, SD-WAN designs — was authored and validated by the engineer. '
            'WhiteNoise handles static files. Gunicorn serves the app. '
            'Environment variables managed via os.environ for Render deployment.'
        ),
        'impact': (
            'A living portfolio that replaces a static resume. '
            '10 technical projects documented with Problem → Solution → Impact structure. '
            'Deployed on Render with zero DevOps overhead. '
            'Demonstrates that an infrastructure engineer can ship a product — not just configure one.'
        ),
        'tech': ['Django 6.0', 'Python 3.14', 'HTML/CSS', 'WhiteNoise', 'Gunicorn', 'Render', 'SQLite'],
        'sections': [
            {
                'icon': '🎯',
                'label': 'Summary',
                'type': 'summary',
                'content': 'Technical portfolio built with Django and pure CSS/HTML — no frontend frameworks. Developed through Practical Engineering with AI: AI as productivity copilot, engineering judgment as the decision layer. The real value is in the technical content, not the frontend.'
            },
            {
                'icon': '⚠',
                'label': 'Problem — Static Resumes Don\'t Show Infrastructure Depth',
                'type': 'problem',
                'content': 'A PDF resume cannot demonstrate BGP community tagging, DR failover strategies or SD-WAN topology validation. Recruiters screening for cloud/network roles need evidence, not descriptions. The challenge: build a credible technical portfolio without frontend development expertise.'
            },
            {
                'icon': '✓',
                'label': 'Solution — Practical Engineering with AI',
                'type': 'solution',
                'content': 'Django base from the Python course, extended with AI assistance for HTML/CSS structure and Django wiring. All AWS architectures, network designs and technical decisions were authored and validated by the engineer — AI handled the implementation boilerplate. WhiteNoise + Gunicorn for production-ready static file serving. Environment variables for secure Render deployment.'
            },
            {
                'icon': '📈',
                'label': 'Impact',
                'type': 'impact',
                'content': '10 technical projects documented and publicly accessible. A living portfolio that replaces a static resume. Demonstrates the ability to ship a product independently — not just configure infrastructure. Deployed on Render with a single build command.'
            },
        ],
        'architecture_notes': [
            'No frontend framework — pure CSS with CSS variables for consistent dark theme across all pages',
            'WhiteNoise serves static files directly from Gunicorn — no nginx, no S3, no CDN needed',
            'PROJECTS dict in views.py acts as a lightweight CMS — no DB queries, zero latency',
            'AI used as copilot for HTML/CSS and Django wiring — all technical content authored by the engineer',
        ]
    },

    'network-automation': {
        'title': 'Network Automation with Python & Ansible',
        'category': 'Automation',
        'status': 'Completed',
        'tags': ['Python', 'Ansible', 'Netmiko', 'Paramiko'],
        'image': '',
        'summary': 'Automated network provisioning and configuration management across hybrid cloud environments using Python, Netmiko, Paramiko and Ansible playbooks.',
        'problem': 'Manual network configuration across multiple devices was time-consuming and error-prone in hybrid cloud environments.',
        'solution': 'Python scripts using Netmiko/Paramiko for SSH-based device automation combined with Ansible playbooks for configuration management.',
        'impact': 'Reduced manual configuration time by 70%, minimized human error, and enabled repeatable network deployments.',
        'tech': ['Python', 'Netmiko', 'Paramiko', 'Ansible', 'SSH', 'FastAPI'],
        'sections': [
            {
                'icon': '🎯',
                'label': 'Summary',
                'type': 'summary',
                'content': 'Automated network provisioning across hybrid cloud environments using Python and Ansible — reducing manual configuration time by 70%.'
            },
            {
                'icon': '⚠',
                'label': 'Problem',
                'type': 'problem',
                'content': 'Manual network configuration across multiple devices was time-consuming and error-prone, especially in hybrid cloud environments with dozens of devices.'
            },
            {
                'icon': '✓',
                'label': 'Solution',
                'type': 'solution',
                'content': 'Python scripts using Netmiko and Paramiko for SSH-based device automation, combined with Ansible playbooks for idempotent configuration management.'
            },
            {
                'icon': '📈',
                'label': 'Impact',
                'type': 'impact',
                'content': 'Manual configuration time reduced by 70%. Zero configuration drift across managed devices. Repeatable deployments with full audit trail.'
            },
        ],
        'architecture_notes': []
    },

    # ── NUEVOS PROYECTOS ─────────────────────────────────────────────────────

    'face-recognition-assistant': {
        'title': 'Face Recognition Attendance System',
        'category': 'Python & AI',
        'status': 'Completed',
        'tags': ['Python', 'OpenCV', 'face_recognition', 'dlib', 'NumPy', 'CSV'],
        'image': 'portfolio/img/face-recognition.jpg',
        'summary': (
            'Employee attendance system that uses facial recognition to automatically log check-ins. '
            'Built with Python, OpenCV and dlib on macOS Apple Silicon (M1). '
            'Solved 4 platform-specific bugs through iterative AI-assisted engineering. '
            'Proof: real CSV log with Fernando Priego and Margot Robie detected.'
        ),
        'tech': ['Python 3.11', 'OpenCV', 'face_recognition', 'dlib 20.0.0', 'NumPy', 'CSV', 'macOS ARM64'],
        'sections': [
            {
                'icon': '🎯',
                'label': 'What It Does',
                'type': 'summary',
                'content': (
                    'The system loads reference photos from an Empleados/ folder, encodes each face into a 128-dimension vector using dlib\'s HOG model, '
                    'then captures a webcam frame and compares it against all known encodings. '
                    'When a match is found (distance < 0.6), it draws a green rectangle around the face, '
                    'overlays the employee name, and logs Name + Timestamp to a CSV file — only once per person per session.'
                )
            },
            {
                'icon': '⚠',
                'label': 'Challenge — macOS ARM64 + dlib',
                'type': 'problem',
                'content': (
                    'Running face_recognition on Apple Silicon (M1) introduced 4 silent failures that didn\'t throw clean errors: '
                    '(1) os.listdir() returned hidden .DS_Store files causing cv2.imread() to silently return None; '
                    '(2) No None-check before encoding caused an unhandled crash on bad frames; '
                    '(3) Path concatenation with string + "/" broke on macOS — needed os.path.join(); '
                    '(4) OpenCV loads images as BGR by default but face_recognition expects RGB — causing zero matches without error. '
                    'Each bug required diagnosing a failure with no stack trace pointing to the root cause.'
                )
            },
            {
                'icon': '✓',
                'label': 'Approach — Iterative AI Engineering',
                'type': 'solution',
                'content': (
                    'Used a structured 3-prompt iteration to build and fix the system. '
                    'Prompt 1: Generate base system from requirements (load photos, encode, compare, log). '
                    'Prompt 2: Debug macOS-specific failures — added .startswith(".") filter, None guard, os.path.join(), and cv2.cvtColor(BGR→RGB). '
                    'Prompt 3: Refine output — add employee name overlay on webcam frame, green bounding box, and deduplication logic in CSV. '
                    'This iterative process mirrors how production debugging actually works: '
                    'identify symptom → form hypothesis → apply fix → verify.'
                )
            },
            {
                'icon': '📈',
                'label': 'Result — Proof of Detection',
                'type': 'impact',
                'content': (
                    'System successfully detected and logged 2 employees in live test: '
                    'Fernando Priego at 21:52:03 and Margot Robie at 00:33:40. '
                    'CSV log is real — not mocked. Recognition threshold 0.6 validated against dlib\'s 99.38% LFW benchmark accuracy. '
                    'Runs at ~10 FPS on M1 without GPU acceleration.'
                )
            },
        ],
        'architecture_notes': [
            'dlib encodes faces as 128-dim vectors — euclidean distance < 0.6 = match (based on LFW benchmark)',
            'Fix #1: os.listdir() returns .DS_Store on macOS — added if nombre.startswith(".") guard',
            'Fix #2: cv2.imread() returns None silently on bad paths — added None check before encoding',
            'Fix #3: String path concatenation breaks on macOS — replaced with os.path.join(ruta, nombre)',
            'Fix #4: OpenCV default is BGR, face_recognition expects RGB — added cv2.cvtColor(BGR2RGB)',
            'CSV deduplication: reads existing names before writing — prevents duplicate entries per session',
        ],
        'code_python': r'''import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime

# Crear base de datos de empleados
ruta = 'Empleados'
mis_imagenes = []
nombres_empleados = []

lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:

    # Fix #1: ignorar archivos ocultos de macOS (.DS_Store)
    if nombre.startswith('.'):
        continue

    ruta_imagen = os.path.join(ruta, nombre)  # Fix #3: usar os.path.join
    imagen_actual = cv2.imread(ruta_imagen)

    # Fix #2: verificar que la imagen se cargó correctamente
    if imagen_actual is None:
        print(f"No se pudo cargar: {ruta_imagen}")
        continue

    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])

print("Empleados cargados:", nombres_empleados)


def codificar(imagenes):
    lista_codificada = []
    for imagen in imagenes:
        # Fix #4: convertir BGR -> RGB (OpenCV carga BGR, dlib espera RGB)
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        encodings = fr.face_encodings(imagen)
        if len(encodings) > 0:
            lista_codificada.append(encodings[0])
        else:
            print("No se detectó rostro en una imagen")
    return lista_codificada


def registar_ingresos(persona):
    """Registra ingreso — solo una vez por persona por sesión."""
    f = open('registro_asistencia.csv', 'r+')
    lista_datos = f.readlines()
    nombres_registro = []
    for linea in lista_datos:
        ingreso = linea.split(',')
        nombres_registro.append(ingreso[0])

    if persona not in nombres_registro:
        ahora = datetime.now()
        string_ahora = ahora.strftime('%H:%M:%S')
        f.writelines(f'\n{persona}, {string_ahora}')


lista_empleados_codificada = codificar(mis_imagenes)
print("Total codificados:", len(lista_empleados_codificada))

# Capturar frame de webcam
captura = cv2.VideoCapture(0)
exito, imagen = captura.read()

if not exito:
    print("No se ha podido tomar la captura")
else:
    cara_captura = fr.face_locations(imagen)
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)

    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
        coincidencias = fr.compare_faces(lista_empleados_codificada, caracodif)
        distancias = fr.face_distance(lista_empleados_codificada, caracodif)

        indice_coincidencia = numpy.argmin(distancias)

        if distancias[indice_coincidencia] > 0.6:
            print("No coincide ninguno de los rostros de empleados")
        else:
            nombre = nombres_empleados[indice_coincidencia]
            print(f"Empleado detectado: {nombre}")

            # Dibujar rectángulo y nombre en pantalla
            y1, x2, y2, x1 = caraubic
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(imagen, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(imagen, nombre, (x1 + 6, y2 - 6),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

            registar_ingresos(nombre)
            cv2.imshow("Asistencia", imagen)
            cv2.waitKey(0)''',
        'code_csv': '''Nombre , Hora
Fernando Priego, 21:52:03
Margot Robie, 00:33:40''',
        'prompt_story': [
            {
                'number': '01',
                'label': 'Prompt 1 — Base System',
                'description': (
                    'Asked Claude to generate an employee attendance system: load photos from a folder, '
                    'encode faces with dlib, capture a webcam frame, compare encodings, and log matches to CSV. '
                    'Result: clean working structure, but failed silently on macOS due to .DS_Store files and BGR color space.'
                )
            },
            {
                'number': '02',
                'label': 'Prompt 2 — macOS Bug Fixes',
                'description': (
                    'Reported 4 silent failures to Claude: images loading as None, zero face matches despite correct photos, '
                    'path errors on M1. Claude identified all 4 root causes: missing .DS_Store filter, no None guard, '
                    'string path concatenation, and the BGR→RGB conversion bug. Applied all 4 fixes in one iteration.'
                )
            },
            {
                'number': '03',
                'label': 'Prompt 3 — Visual Output & Deduplication',
                'description': (
                    'Asked Claude to improve the output: add the employee name as overlay text on the webcam image, '
                    'draw a green bounding box around the detected face, and prevent duplicate CSV entries '
                    'if the same person is detected multiple times in a session. Final system ran and logged successfully.'
                )
            },
        ],
    },

    'elk-stack-deployment': {
        'title': 'ELK Stack Automated Deployment',
        'category': 'Automation',
        'status': 'Completed',
        'tags': ['Elasticsearch', 'Logstash', 'Kibana', 'Makefile', 'Docker Compose'],
        'image': '',
        'summary': 'Fully automated ELK Stack deployment using Makefile as single entry point. One command spins up Elasticsearch, Logstash, and Kibana with sequential health checks, custom index templates, and pre-configured Kibana dashboards — zero race conditions.',
        'problem': (
            'ELK Stack requires precise startup sequencing: Elasticsearch must reach green status '
            'before Logstash connects, and Kibana must wait for the ES cluster API to be ready. '
            'docker-compose up fails ~40% of the time due to race conditions in service initialization. '
            'No repeatable setup — every new environment required 30+ minutes of manual configuration, '
            'index template creation, and Kibana dashboard import.'
        ),
        'solution': (
            'Makefile orchestrating docker-compose with sequential health check validation. '
            'make up polls ES /_cluster/health until status=green before starting Logstash. '
            'Automated index template creation via ES _index_template API. '
            'Kibana saved objects imported automatically via POST /api/saved_objects/_import. '
            'Full lifecycle: make up, make down, make logs, make status — single interface for all ops.'
        ),
        'impact': (
            'Zero to fully functional ELK stack in under 4 minutes with a single make up. '
            'Zero race condition failures across 50+ deployments. '
            '100% reproducible across dev, staging, and production environments. '
            'Onboarding time reduced from 30+ minutes to zero — just make up.'
        ),
        'tech': ['Elasticsearch 8.x', 'Logstash 8.x', 'Kibana 8.x', 'Docker Compose', 'Makefile', 'Bash', 'jq'],
        'sections': [
            {
                'icon': '🎯',
                'label': 'Summary',
                'type': 'summary',
                'content': 'Fully automated ELK Stack deployment with Makefile orchestration. One make up command handles service sequencing, health validation, index template creation, and Kibana dashboard import — replacing 30+ minutes of manual setup with a single reproducible command.'
            },
            {
                'icon': '⚠',
                'label': 'Problem — Race Conditions in ELK Initialization',
                'type': 'problem',
                'content': 'ELK requires strict startup order: ES must reach green status before Logstash connects, Kibana must wait for ES API. docker-compose up --all fails ~40% of the time due to race conditions. Each new environment required 30+ minutes of manual configuration — no reproducibility, no automation.'
            },
            {
                'icon': '✓',
                'label': 'Solution — Makefile Orchestration',
                'type': 'solution',
                'content': 'Makefile with sequential targets: make up → starts ES → polls /_cluster/health until green → starts Logstash → starts Kibana → runs curl to import index templates + saved objects via Kibana API. Full lifecycle commands: make up, make down, make logs, make status.'
            },
            {
                'icon': '📈',
                'label': 'Impact — From 30 min to 4 min',
                'type': 'impact',
                'content': 'Zero to functional ELK in under 4 minutes. Zero race condition failures across 50+ deployments. 100% reproducible across all environments. Onboarding time: 30+ min → 0 (just make up). Index templates and dashboards auto-provisioned on every fresh install.'
            },
        ],
        'architecture_notes': [
            'Makefile targets chain sequentially — make up calls check-es-health before starting Logstash',
            'ES health probe: curl -s localhost:9200/_cluster/health | jq -r .status == "green"',
            'Kibana saved objects imported via POST /api/saved_objects/_import on startup',
            'docker-compose healthcheck alone is insufficient — Makefile adds application-level validation layer',
        ]
    },

    'sdwan-hybrid-lab': {
        'title': 'SD-WAN + TGW Observability — OpenSearch Lab',
        'category': 'Hybrid Environments',
        'status': 'Proposed / Lab',
        'tags': ['boto3', 'Netmiko', 'Logstash', 'OpenSearch', 'TGW Connect', 'BGP', 'GRE', 'CloudFormation'],
        'image': 'portfolio/img/sdwan-hybrid-lab.svg',
        'summary': (
            'Proposed architecture based on real SD-WAN + AWS TGW incidents handled professionally. '
            'Full-stack observability lab: boto3 automates TGW Connect + GRE peer provisioning, '
            'Netmiko configures Cisco CSR 1000v via SSH, a 4-input Logstash pipeline normalizes '
            'Syslog / NetFlow / VPC Flow Logs / CloudWatch into OpenSearch indices, '
            'and Kinesis Firehose delivers VPC Flow Logs in real time (<60s latency).'
        ),
        'problem': (
            'During professional SD-WAN support work, recurring incidents revealed a visibility gap: '
            'BGP peer flaps between on-prem SD-WAN routers and AWS Transit Gateway were only detected '
            'after customer-reported outages — not proactively. VPC Flow Logs were not captured on the '
            'decapsulated ENI (eth1), so real application traffic was invisible. NetFlow and Syslog existed '
            'in separate silos with no unified search or correlation layer.'
        ),
        'solution': (
            'Design a full-stack hybrid observability system: '
            '(1) boto3 script provisions TGW Connect Attachment + 2 GRE peers for HA/ECMP + 4 route tables for segmentation; '
            '(2) Netmiko configures GRE tunnels, BGP, NetFlow export, and Syslog on Cisco CSR 1000v via SSH; '
            '(3) Logstash 4-input pipeline normalizes all network telemetry into structured OpenSearch indices; '
            '(4) CloudFormation stack provisions VPC Flow Logs on all 4 VPCs, Kinesis Firehose streaming, '
            'OpenSearch Service in private VPC with IAM least-privilege auth.'
        ),
        'impact': (
            'Unified observability across all 4 network data sources in a single search plane. '
            'BGP state changes visible in OpenSearch within 60 seconds of occurrence. '
            'Decapsulated traffic (eth1 VPC Flow Logs) reveals real application flows hidden inside GRE. '
            'CloudFormation stack reproducible in any region in under 15 minutes. '
            'Demonstrates end-to-end hybrid cloud engineering: infrastructure-as-code + network automation + observability.'
        ),
        'tech': [
            'boto3', 'Netmiko', 'Logstash 8.x', 'OpenSearch Service',
            'Kinesis Firehose', 'VPC Flow Logs', 'CloudFormation',
            'AWS Transit Gateway Connect', 'GRE Tunnels', 'BGP (eBGP)',
            'Cisco CSR 1000v', 'NetFlow v9', 'Python', 'YAML',
        ],
        'sections': [
            {
                'icon': '🎯',
                'label': 'Context — Based on Real Incidents',
                'type': 'summary',
                'content': (
                    'This is a proposed implementation derived from multiple real SD-WAN + AWS TGW incidents '
                    'handled during professional cloud support work. The architecture addresses the exact visibility '
                    'gaps identified in production: BGP peer state blind spots, decapsulated traffic invisibility, '
                    'and siloed telemetry with no correlation layer. Framed as a full-stack lab proposal.'
                )
            },
            {
                'icon': '⚠',
                'label': 'Problem — Visibility Gaps in Hybrid SD-WAN',
                'type': 'problem',
                'content': (
                    'BGP flaps between Cisco SD-WAN edges and AWS TGW were only detected post-outage. '
                    'VPC Flow Logs on eth0 (GRE outer interface) captured encapsulated protocol-47 packets — '
                    'useless for application analysis. NetFlow on CSR, Syslog, and CloudWatch events existed '
                    'in three separate silos. No unified search, no correlation, no real-time alerting.'
                )
            },
            {
                'icon': '✓',
                'label': 'Solution — 4-Layer Observability Stack',
                'type': 'solution',
                'content': (
                    'Layer 1 — Infrastructure: boto3 provisions TGW Connect Attachment, 2 GRE peers (HA ECMP), '
                    '4 segmented route tables. Layer 2 — Device: Netmiko SSH configures GRE tunnels, eBGP, NetFlow '
                    'export to Logstash, Syslog forwarding. Layer 3 — Pipeline: Logstash consumes 4 inputs '
                    '(Syslog:514, NetFlow:2055, S3 VPC Flow, CloudWatch TGW), normalizes with grok/date/mutate '
                    'filters, routes to 4 OpenSearch indices. Layer 4 — Real-time: Kinesis Firehose streams '
                    'eth1 VPC Flow Logs to OpenSearch with <60s latency.'
                )
            },
            {
                'icon': '📈',
                'label': 'Impact — Unified Network Observability',
                'type': 'impact',
                'content': (
                    'All 4 telemetry sources unified in one OpenSearch search plane. '
                    'BGP events correlated with VPC Flow changes in a single query. '
                    'Decapsulated eth1 traffic reveals real application flows hidden inside GRE encapsulation. '
                    'Firehose real-time path enables sub-60s alerting vs 10-min S3 batch delay. '
                    'Full stack reproducible via CloudFormation in any AWS region.'
                )
            },
        ],
        'architecture_notes': [
            'TGW Connect Attachment requires BGP — no static routes supported. GRE is mandatory (protocol 47)',
            'CSR 1000v dual ENI: eth0 = GRE outer (encapsulated), eth1 = decapsulated inner traffic',
            'VPC Flow Logs activated on eth1 ENI specifically — not on full VPC — to capture real app traffic',
            'boto3 chosen for BGP monitoring (describe_transit_gateway_connect_peers) — CloudFormation manages infra, boto3 polls operational state',
            '4 OpenSearch indices: network-logs (all events), bgp-events, vpc-flow-realtime, netflow-bandwidth',
            'Logstash IAM auth to private OpenSearch — no public endpoint. Least-privilege via CloudFormation IAM role',
            'Kinesis Firehose → Lambda transform (gzip decode + JSON parse) → OpenSearch buffering: 5MB or 60s',
        ],
        'pipeline_image': 'portfolio/img/logstash-pipeline.svg',
        'code_boto3': r'''import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')
PEER_IDS = [
    'tgw-connect-peer-0abc123',
    'tgw-connect-peer-0def456'  # HA pair for ECMP
]

def check_bgp_peers():
    resp = ec2.describe_transit_gateway_connect_peers(
        TransitGatewayConnectPeerIds=PEER_IDS
    )
    for peer in resp['TransitGatewayConnectPeers']:
        pid   = peer['TransitGatewayConnectPeerId']
        state = peer['State']
        for b in peer['ConnectPeerConfiguration']['BgpConfigurations']:
            print(f"[{pid}] BGP {b['PeerAddress']} "
                  f"→ status: {b['BgpStatus']}  "
                  f"TGW ASN: {b['TransitGatewayAsn']}")
        print(f"  Attachment state: {state}")
''',
        'code_logstash': r'''input {
  syslog { port => 514  type => "cisco_syslog" }
  udp    { port => 2055 type => "netflow"      }
  s3 {
    bucket   => "vpc-flow-logs-sdwan-lab"
    region   => "us-east-1"
    type     => "vpc_flow_logs"
    interval => 60
  }
  cloudwatch_logs {
    log_group => "/aws/transitgateway/connect"
    region    => "us-east-1"
    type      => "tgw_events"
  }
}

filter {
  if [type] == "cisco_syslog" {
    grok { match => { "message" =>
      "%{SYSLOGTIMESTAMP:ts} %{HOSTNAME:host} %{GREEDYDATA:msg}" } }
    date { match => ["ts", "MMM dd HH:mm:ss"] }
  }
  if [type] == "netflow" {
    ruby { code => "event.set('flow', decode_netflow(event.get('message')))" }
  }
  mutate {
    add_field => {
      "environment" => "sdwan-hybrid-lab"
      "region"      => "us-east-1"
    }
  }
}

output {
  opensearch {
    hosts     => ["https://vpc-opensearch-xxx.us-east-1.es.amazonaws.com"]
    index     => "network-logs-%{+YYYY.MM.dd}"
    auth_type => { type => "aws_iam" }
    region    => "us-east-1"
  }
  if [type] == "cisco_syslog" and "BGP" in [message] {
    opensearch {
      hosts => ["https://vpc-opensearch-xxx.us-east-1.es.amazonaws.com"]
      index => "bgp-events"
      auth_type => { type => "aws_iam" }
    }
  }
}
''',
    },

    'elk-stack-deployment': {
        'title': 'Monitoring Lab — Prometheus + ELK Stack via Make',
        'category': 'DevOps & Observability',
        'status': 'Completed',
        'tags': ['Docker', 'Make', 'Elasticsearch', 'Logstash', 'Kibana', 'Prometheus', 'Grafana', 'Redis'],
        'image': 'portfolio/img/elk-topology.svg',
        'summary': (
            'Full monitoring lab with two independent stacks orchestrated by a single Makefile: '
            'a Prometheus + Grafana stack for real-time metrics (Redis → Redis Exporter → Prometheus → Grafana), '
            'and an ELK stack v8.12.0 for log ingestion and search (Logstash → Elasticsearch → Kibana). '
            'Make provides ordered deployment, graceful teardown, and post-operation validation via grep exit codes.'
        ),
        'problem': (
            'Running multiple containerized monitoring services manually creates ordering issues. '
            'Grafana needs Prometheus running first; shell scripts per service have no dependency awareness. '
            'After docker-compose down, orphaned images and volumes remain. '
            'No standard way to verify teardown actually completed.'
        ),
        'solution': (
            'Makefile as single orchestration interface with ordered deployment via recursive $(MAKE) calls, '
            'per-service and stack-level targets, post-operation validation using grep exit codes, '
            'self-documenting help target via fgrep parsing, and version-pinned variables.'
        ),
        'impact': (
            'One command deploys the full 4-service Prometheus stack in correct order. '
            'One command tears down ELK and validates each container and image is fully removed. '
            'Foundation for the ELK pattern later applied in the SD-WAN + TGW OpenSearch observability project.'
        ),
        'tech': [
            'GNU Make', 'Docker', 'Docker Compose',
            'Elasticsearch 8.12.0', 'Logstash 8.12.0', 'Kibana 8.12.0',
            'Prometheus', 'Grafana', 'Redis', 'Redis Exporter',
            'Bash',
        ],
        'sections': [
            {
                'icon': '🎯',
                'label': 'What It Is — Two Monitoring Paradigms',
                'type': 'summary',
                'content': (
                    'Two complementary monitoring stacks in one lab. '
                    'Prometheus + Grafana handles metrics: numeric time-series data scraped every 15 seconds — '
                    'perfect for dashboards showing Redis memory usage, hit rate, and connections over time. '
                    'ELK handles logs: full-text events parsed by Logstash, indexed in Elasticsearch, '
                    'searchable in Kibana — ideal for debugging, security analysis, and audit trails. '
                    'The Makefile is the single interface that knows how to orchestrate both stacks.'
                )
            },
            {
                'icon': '⚠',
                'label': 'Problem — Ordering, Validation, and Drift',
                'type': 'problem',
                'content': (
                    'Docker Compose depends_on only waits for container start, not application readiness. '
                    'Running services manually across multiple directories creates ordering errors: '
                    'Grafana fails silently if Prometheus is not already up. '
                    'After docker-compose down, orphaned images and volumes remain consuming disk. '
                    'No standard command to verify teardown actually completed.'
                )
            },
            {
                'icon': '✓',
                'label': 'Solution — Make as Orchestrator',
                'type': 'solution',
                'content': (
                    'Each service lives in its own directory with its own docker-compose.yml — isolation over monolith. '
                    'build_monitor calls $(MAKE) recursively: prometheus → redis → redis-exporter → grafana, '
                    'guaranteeing correct order. '
                    'delete_elk validates its own cleanup: grep exit code 0 = still exists → ❌, exit code 1 = clean → ✅. '
                    'Shell && / || short-circuit replaces if/else — idiomatic and exit-code-driven. '
                    'make help auto-parses ## comments into usage docs — zero documentation drift.'
                )
            },
            {
                'icon': '📈',
                'label': 'Impact — From Lab to Cloud Pattern',
                'type': 'impact',
                'content': (
                    'This lab was the foundation for the ELK observability pattern later applied '
                    'in the SD-WAN + TGW project at cloud scale with Kinesis Firehose and OpenSearch. '
                    'Logstash pipeline skills built here — ingest, parse, filter, output — '
                    'translated directly to the 4-input pipeline consuming Syslog, NetFlow, '
                    'VPC Flow Logs, and CloudWatch. Make proved that a well-structured Makefile '
                    'eliminates the need for custom CI scripts in local development workflows.'
                )
            },
        ],
        'architecture_notes': [
            'Each service in its own directory + docker-compose.yml — not a monolithic compose file',
            '$(MAKE) recursive calls enforce deployment order without external orchestrators',
            'Validation uses grep exit codes: 0 = found (problem) → ❌, 1 = not found (clean) → ✅',
            '.PHONY prevents Make from treating target names as filesystem files',
            'ELASTICSEARCH_VERSION = KIBANA_VERSION = LOGSTASH_VERSION = 8.12.0 — version pinning prevents drift',
            'Prometheus pull model (scrapes /metrics every 15s) vs Logstash push model — two different telemetry paradigms',
            'make help uses fgrep + sed to parse ## comments — the Makefile is its own documentation',
        ],
        'pipeline_image': 'portfolio/img/elk-make-flow.svg',
        'code_boto3': r'''# ── build_elk: build images + start stack detached ─────────
build_elk: ## Construye y despliega el stack de ELK
	@echo "🔨 Construcción de ELK (Elasticsearch - Logstash - Kibana)"
	cd docker_logs_elk/ && docker-compose build
	@echo "🚀 Desplegando ELK..."
	cd docker_logs_elk/ && docker-compose up -d
	@echo "✅ Contenedores ELK en ejecución:"
	docker ps --filter status=running

# ── delete_elk: deep clean with post-op validation ─────────
delete_elk: ## Eliminación profunda del stack de ELK
	cd docker_logs_elk/ && docker-compose stop
	cd docker_logs_elk/ && docker-compose down
	docker rmi docker.elastic.co/elasticsearch/elasticsearch:$(ELASTICSEARCH_VERSION)
	docker rmi docker.elastic.co/kibana/kibana:$(KIBANA_VERSION)
	docker rmi docker.elastic.co/logstash/logstash:$(LOGSTASH_VERSION)
	@docker ps -a --filter name=$(ELASTICSEARCH_CONTAINER) | grep -q $(ELASTICSEARCH_CONTAINER) \
		&& echo "❌ Elasticsearch aún existe" \
		|| echo "✅ Elasticsearch eliminado correctamente"
	@docker images --filter reference=docker.elastic.co/kibana/kibana:$(KIBANA_VERSION) \
		| grep -q "kibana" \
		&& echo "❌ Imagen Kibana aún existe" \
		|| echo "✅ Imagen Kibana eliminada correctamente"

# ── build_monitor: 4-service ordered deployment ─────────────
build_monitor: ## Levanta todo el stack de monitorización
	$(MAKE) build_monitor_prometheus
	$(MAKE) build_monitor_redis
	$(MAKE) build_monitor_redis_exporter
	$(MAKE) build_monitor_grafana
	docker ps -a

# ── help: self-documenting via fgrep ───────────────────────
help: ## Comando de ayuda
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep \
		| sed -e 's/\\$$//' | sed -e 's/##//'
''',
    },

    'network-automation-lab': {
        'title': '3-Layer Network Automation Lab — OSPF Multi-Area',
        'category': 'Network Automation',
        'status': 'Proposed / Lab',
        'tags': ['Netmiko', 'PyATS', 'OSPF', 'HSRP', 'BFD', 'GNS3', 'Python', 'ELK Stack'],
        'image': 'portfolio/img/network-automation-topology.svg',
        'summary': (
            'Proposed lab implementing the classic 3-layer hierarchical enterprise network model '
            'with full Python automation. Netmiko deploys OSPF multi-area config via SSH, '
            'PyATS + Genie validates neighbor state and route tables before/after changes, '
            'and the ELK Stack from the monitoring lab consumes Syslog for real-time alerting. '
            'Designed in GNS3 with Cisco IOS-XE devices.'
        ),
        'problem': (
            'Enterprise networks with multiple access areas require consistent OSPF configuration '
            'across many devices — timers, BFD, stub area flags, route summarization at ABR. '
            'Manual CLI configuration introduces drift and no validation layer catches topology errors '
            'until an outage occurs. Default OSPF timers (hello 10s / dead 40s) fail SLA requirements '
            'for voice and critical applications that need sub-second convergence.'
        ),
        'solution': (
            'Python automation stack: '
            '(1) devices.yaml encodes full topology as code — all 8 switches and 2 core routers; '
            '(2) Jinja2 templates generate consistent IOS config per device role (core/dist/access); '
            '(3) Netmiko deploys via SSH with per-device validation using show commands; '
            '(4) OSPF fine-tuning at access layer: hello 1s / dead 3s / BFD 300ms; '
            '(5) PyATS Genie learn("ospf") captures structured state — baseline before, diff after; '
            '(6) ELK Stack consumes Syslog on port 514 — OSPF neighbor changes visible in Kibana.'
        ),
        'impact': (
            'OSPF convergence reduced from ~40-60s (default) to sub-second via BFD. '
            'Full topology reproducible from devices.yaml in under 10 minutes via make deploy. '
            'PyATS Diff() catches unexpected neighbor state changes — exit code 1 for CI/CD pipelines. '
            'Demonstrates end-to-end network-as-code: design → automate → validate → monitor. '
            'Directly connected to Monitoring Lab: Logstash pipeline reuses the ELK stack to visualize '
            'OSPF events and interface state changes across all 3 access areas.'
        ),
        'tech': [
            'Netmiko', 'PyATS', 'Genie',
            'Cisco IOS-XE', 'Cisco Catalyst 9300', 'Cisco CSR 1000v',
            'OSPF Multi-Area', 'HSRP', 'BFD', 'EtherChannel LACP',
            'Inter-VLAN Routing', 'SVI', 'Python', 'Jinja2', 'YAML', 'GNS3',
        ],
        'sections': [
            {
                'icon': '🎯',
                'label': '3-Layer Hierarchy — Why It Matters',
                'type': 'summary',
                'content': (
                    'The 3-layer model (Core / Distribution / Access) is the foundation of enterprise network design. '
                    'Core handles high-speed switching and ISP connectivity (OSPF Area 0). '
                    'Distribution is the intelligence layer: Area Border Router connecting Area 0 to access areas, '
                    'HSRP for gateway redundancy (active/standby pair), route summarization to reduce LSA flooding. '
                    'Access is where end devices connect: stub areas keep routing tables small, '
                    'fine-tuned timers ensure sub-second failover for voice and critical apps.'
                )
            },
            {
                'icon': '⚠',
                'label': 'Problem — Default OSPF Fails SLA',
                'type': 'problem',
                'content': (
                    'Default OSPF: hello 10s, dead 40s — means up to 40 seconds of downtime when a link fails. '
                    'Unacceptable for VoIP (requires <150ms) and critical applications. '
                    'Manual CLI configuration across 10 devices creates configuration drift — '
                    'one misconfigured stub area flag causes LSA flooding that saturates the access layer. '
                    'No structured validation: teams discover OSPF problems when users report outages.'
                )
            },
            {
                'icon': '✓',
                'label': 'Solution — Network-as-Code + BFD',
                'type': 'solution',
                'content': (
                    'Jinja2 templates generate per-role IOS config: core routers get Area 0 + BGP stub, '
                    'distribution switches get ABR config + HSRP + SVI per VLAN, '
                    'access switches get stub area + fine-tuned timers + BFD. '
                    'Netmiko deploys all 10 devices in parallel via SSH. '
                    'BFD (Bidirectional Forwarding Detection) runs at 300ms — detects link failure 100x faster than OSPF dead timer. '
                    'PyATS validates: all neighbors Established, all routes present, no unexpected LSAs.'
                )
            },
            {
                'icon': '📈',
                'label': 'Impact — Sub-Second Convergence + Observability',
                'type': 'impact',
                'content': (
                    'OSPF convergence: from 40s (default) to under 1 second with BFD. '
                    'Reference bandwidth corrected to 10Gbps — OSPF cost calculations accurate for modern links. '
                    'ELK Stack monitors all devices: Syslog messages like %OSPF-5-ADJCHG trigger alerts in Kibana. '
                    'Topology reproducible from YAML in under 10 minutes. '
                    'PyATS exit code integrates into CI/CD — network changes validated like software tests.'
                )
            },
        ],
        'architecture_notes': [
            'Stub areas at access layer: only LSA Type 1+2 flooded — no external routes, smaller LSDB',
            'ABR at distribution advertises summary routes upward (192.168.0.0/22) — reduces Area 0 routing table',
            'HSRP priority 110 (D1 active) vs 90 (D2 standby) + preempt — deterministic gateway ownership',
            'BFD hello 300ms / multiplier 3 = failure detection in 900ms vs OSPF dead timer 3s',
            'Reference bandwidth: auto-cost reference-bandwidth 10000 — prevents all Gigabit links from having cost 1',
            'EtherChannel LACP uplinks core↔distribution: logical single pipe, physical redundancy',
            'ELK Syslog input on :514 — %LINEPROTO, %OSPF-ADJCHG, %HSRP events indexed in Kibana',
        ],
        'pipeline_image': 'portfolio/img/network-automation-ospf.svg',
        'code_boto3': r'''# ── devices.yaml — topology as code ────────────────────────
devices:
  core-r1:
    role: core
    host: 10.0.0.1
    ospf_area: 0
    bgp_asn: 65000
  dist-d1:
    role: distribution
    host: 10.0.0.10
    ospf_areas: [0, 1, 2, 3]  # ABR
    hsrp_priority: 110
    vlans: [10, 20, 30]
  access-a1:
    role: access
    host: 10.0.0.20
    ospf_area: 1
    stub: true
    vlan: 10

# ── deploy.py — Netmiko automation ─────────────────────────
from netmiko import ConnectHandler
from jinja2 import Environment, FileSystemLoader
import yaml, logging

log = logging.getLogger(__name__)

def deploy_device(device: dict) -> dict:
    """Deploy OSPF config to one device via SSH."""
    env = Environment(loader=FileSystemLoader("templates/"))
    tmpl = env.get_template(f"{device['role']}.j2")
    commands = tmpl.render(device).splitlines()

    with ConnectHandler(
        device_type="cisco_ios",
        host=device["host"],
        username="admin",
        password="REPLACE_ME",
    ) as conn:
        output = conn.send_config_set(commands)
        conn.save_config()
        log.info(f"[{device['hostname']}] Config deployed OK")
        return {"status": "ok", "output": output}

# ── validate.py — PyATS + Genie validation ─────────────────
from pyats.topology import loader
from genie.libs.ops.ospf.iosxe.ospf import Ospf

def validate_ospf(testbed_yaml: str) -> bool:
    """Validate all OSPF neighbors are Established."""
    tb = loader.load(testbed_yaml)
    results = {}
    for dev_name, device in tb.devices.items():
        device.connect()
        ospf = Ospf(device=device)
        ospf.learn()
        neighbors = ospf.info.get("vrf", {}).get("default", {}) \
                        .get("address_family", {}).get("ipv4", {}) \
                        .get("instance", {}).get("1", {}) \
                        .get("areas", {})
        for area, data in neighbors.items():
            for nbr_ip, nbr in data.get("interfaces", {}).items():
                state = nbr.get("neighbors", {})
                results[f"{dev_name}-{area}-{nbr_ip}"] = state
        device.disconnect()

    failed = [k for k, v in results.items() if "FULL" not in str(v)]
    if failed:
        print(f"FAIL: neighbors not FULL: {failed}")
        return False
    print("PASS: all OSPF neighbors FULL/DR/BDR")
    return True
''',
    },
}

