#!/usr/bin/env python3
"""
AUTOAGENT - Self-Sustaining AI Agent Company
=============================================
Core Orchestrator: Manages multiple AI agents that generate revenue,
track performance, and report results.

The agents:
1. CONTENT_AGENT  - Generates SEO content with affiliate links (short-term revenue)
2. MARKET_AGENT   - Researches opportunities and market trends
3. SERVICE_AGENT  - Provides automated AI services to clients
4. MONITOR_AGENT  - Tracks performance and optimizes strategy

Architecture: Event-driven, cron-scheduled, self-improving.
"""

import os
import sys
import json
import time
import logging
import argparse
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass, field, asdict

# ============================================================
# CONFIGURATION
# ============================================================

BASE_DIR = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONTENT_DIR = BASE_DIR / "content"
DATA_DIR = BASE_DIR / "data"
LOGS_DIR = BASE_DIR / "logs"
SCRIPTS_DIR = BASE_DIR / "scripts"
AFFILIATE_DIR = BASE_DIR / "affiliate"

# Ensure directories exist
for d in [CONTENT_DIR, DATA_DIR, LOGS_DIR, CONTENT_DIR / "generated", CONTENT_DIR / "published"]:
    d.mkdir(parents=True, exist_ok=True)

# ============================================================
# DATA MODELS
# ============================================================

@dataclass
class AgentTask:
    name: str
    agent_type: str  # content, market, service, monitor
    status: str = "pending"  # pending, running, completed, failed
    output: str = ""
    error: str = ""
    created_at: str = ""
    completed_at: str = ""

@dataclass
class RevenueRecord:
    source: str
    amount: float
    currency: str = "USD"
    timestamp: str = ""
    description: str = ""

@dataclass
class AgentReport:
    agent_name: str
    period: str
    tasks_completed: int = 0
    tasks_failed: int = 0
    revenue_generated: float = 0.0
    content_produced: int = 0
    leads_generated: int = 0
    summary: str = ""

# ============================================================
# CORE ORCHESTRATOR
# ============================================================

class AutoAgentOrchestrator:
    """
    Central orchestrator that coordinates all AI agents.
    Each agent runs as a self-contained module that produces outputs.
    The orchestrator tracks everything and generates daily reports.
    """
    
    def __init__(self):
        self.logger = self._setup_logging()
        self.task_history: List[AgentTask] = []
        self.revenue_log: List[RevenueRecord] = []
        self._load_state()
    
    def _setup_logging(self):
        log_file = LOGS_DIR / f"orchestrator_{datetime.now().strftime('%Y%m%d')}.log"
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s [%(levelname)s] %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler(sys.stdout)
            ]
        )
        return logging.getLogger('AutoAgent')
    
    def _load_state(self):
        """Load previous state if exists."""
        state_file = DATA_DIR / "orchestrator_state.json"
        if state_file.exists():
            try:
                with open(state_file) as f:
                    state = json.load(f)
                self.revenue_log = [RevenueRecord(**r) for r in state.get('revenue', [])]
                self.task_history = [AgentTask(**t) for t in state.get('tasks', [])]
                self.logger.info(f"Loaded state: {len(self.revenue_log)} revenue records, {len(self.task_history)} tasks")
            except Exception as e:
                self.logger.warning(f"Could not load state: {e}")
    
    def _save_state(self):
        """Save current state."""
        state_file = DATA_DIR / "orchestrator_state.json"
        try:
            state = {
                'revenue': [asdict(r) for r in self.revenue_log],
                'tasks': [asdict(t) for t in self.task_history[-100:]],  # keep last 100
                'last_updated': datetime.now().isoformat()
            }
            with open(state_file, 'w') as f:
                json.dump(state, f, indent=2, ensure_ascii=False)
        except Exception as e:
            self.logger.error(f"Failed to save state: {e}")
    
    def log_revenue(self, source: str, amount: float, currency: str = "USD", description: str = ""):
        """Record a revenue event."""
        record = RevenueRecord(
            source=source,
            amount=amount,
            currency=currency,
            timestamp=datetime.now().isoformat(),
            description=description
        )
        self.revenue_log.append(record)
        self._save_state()
        self.logger.info(f"💰 REVENUE: {amount} {currency} from {source}")
    
    def log_task(self, task: AgentTask):
        """Record a task completion."""
        if task.completed_at:
            task.completed_at = datetime.now().isoformat()
        self.task_history.append(task)
        self._save_state()
        status_icon = "✅" if task.status == "completed" else "❌" if task.status == "failed" else "⏳"
        self.logger.info(f"{status_icon} Task [{task.name}] ({task.agent_type}): {task.status}")
    
    def run_agent(self, agent_type: str, task_name: str) -> AgentTask:
        """Run a single agent task."""
        task = AgentTask(
            name=task_name,
            agent_type=agent_type,
            status="running",
            created_at=datetime.now().isoformat()
        )
        
        try:
            if agent_type == "content":
                # Content generation is handled by the AI agent (me)
                # This orchestrator just tracks it
                task.status = "completed"
                task.output = f"Content generation task queued: {task_name}"
            
            elif agent_type == "market":
                # Market research placeholder
                task.status = "completed"
                task.output = f"Market research queued: {task_name}"
            
            elif agent_type == "monitor":
                # Generate daily report
                report = self.generate_report()
                task.status = "completed"
                task.output = json.dumps(report, indent=2, ensure_ascii=False)
            
            else:
                task.status = "failed"
                task.error = f"Unknown agent type: {agent_type}"
        
        except Exception as e:
            task.status = "failed"
            task.error = str(e)
            self.logger.error(f"Agent task failed: {e}")
        
        self.log_task(task)
        return task
    
    def generate_report(self) -> AgentReport:
        """Generate a performance report."""
        now = datetime.now()
        today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
        
        # Count today's tasks
        today_tasks = [t for t in self.task_history if t.created_at >= today_start.isoformat()]
        tasks_completed = sum(1 for t in today_tasks if t.status == "completed")
        tasks_failed = sum(1 for t in today_tasks if t.status == "failed")
        
        # Count today's revenue
        today_revenue = sum(r.amount for r in self.revenue_log 
                          if r.timestamp >= today_start.isoformat())
        
        # Count content produced
        content_dirs = list((CONTENT_DIR / "generated").iterdir()) if (CONTENT_DIR / "generated").exists() else []
        content_count = len([d for d in content_dirs 
                           if d.name.startswith(now.strftime("%Y-%m-%d"))])
        
        report = AgentReport(
            agent_name="AutoAgent",
            period=now.strftime("%Y-%m-%d"),
            tasks_completed=tasks_completed,
            tasks_failed=tasks_failed,
            revenue_generated=today_revenue,
            content_produced=content_count,
            leads_generated=0,
            summary=self._generate_summary(tasks_completed, tasks_failed, today_revenue, content_count)
        )
        
        # Save report
        report_path = DATA_DIR / f"report_{now.strftime('%Y%m%d')}.json"
        with open(report_path, 'w') as f:
            json.dump(asdict(report), f, indent=2, ensure_ascii=False)
        
        return report
    
    def _generate_summary(self, completed, failed, revenue, content):
        """Generate a human-readable summary."""
        parts = []
        parts.append(f"📊 Daily Report - {datetime.now().strftime('%Y-%m-%d')}")
        parts.append(f"───")
        parts.append(f"Tasks Completed: {completed}")
        if failed > 0:
            parts.append(f"Tasks Failed: {failed} ⚠️")
        parts.append(f"Revenue Today: ${revenue:.2f}")
        parts.append(f"Content Produced: {content} articles")
        
        # Suggestions based on data
        if content > 0:
            parts.append(f"✅ Content pipeline active")
        if revenue > 0:
            parts.append(f"💰 Revenue generating")
        if failed > 0:
            parts.append(f"⚠️ {failed} tasks failed - may need attention")
        
        return "\n".join(parts)
    
    def get_total_revenue(self) -> float:
        return sum(r.amount for r in self.revenue_log)
    
    def get_content_stats(self) -> Dict:
        """Get statistics about generated content."""
        stats = {
            "total_articles": 0,
            "total_words": 0,
            "by_niche": {},
            "by_platform": {}
        }
        
        # Scan content directories
        gen_dir = CONTENT_DIR / "generated"
        if gen_dir.exists():
            for d in sorted(gen_dir.iterdir()):
                if d.is_dir():
                    article_files = list(d.glob("article_*.md"))
                    for article in article_files:
                        stats["total_articles"] += 1
                        try:
                            words = len(article.read_text().split())
                            stats["total_words"] += words
                        except:
                            pass
        
        return stats


# ============================================================
# MAIN
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="AutoAgent Orchestrator")
    parser.add_argument("--run", choices=["content", "market", "monitor", "all"], 
                       default="monitor", help="Which agent to run")
    parser.add_argument("--task", default="daily_run", help="Task name")
    parser.add_argument("--report", action="store_true", help="Generate and print report")
    
    args = parser.parse_args()
    
    orchestrator = AutoAgentOrchestrator()
    
    if args.report:
        report = orchestrator.generate_report()
        print(report.summary)
        return
    
    if args.run == "all":
        for agent_type in ["content", "market", "monitor"]:
            orchestrator.run_agent(agent_type, f"{agent_type}_{datetime.now().strftime('%H%M%S')}")
    else:
        orchestrator.run_agent(args.run, args.task)
    
    # Print summary
    stats = orchestrator.get_content_stats()
    total_rev = orchestrator.get_total_revenue()
    
    print("\n" + "=" * 50)
    print("AUTOAGENT STATUS REPORT")
    print("=" * 50)
    print(f"Total Revenue: ${total_rev:.2f}")
    print(f"Total Articles: {stats['total_articles']}")
    print(f"Total Words: {stats['total_words']:,}")
    print(f"Tasks Tracked: {len(orchestrator.task_history)}")
    print("=" * 50)

if __name__ == "__main__":
    main()
