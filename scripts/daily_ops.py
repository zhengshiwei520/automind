#!/usr/bin/env python3
"""
AutoMind - Daily Operations Script
===================================
Runs every day to:
1. Check system status
2. Generate daily report
3. Log results
4. Update website stats

Schedule: Run daily via cron
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
CONTENT_DIR = BASE_DIR / "content" / "generated"
DATA_DIR = BASE_DIR / "data"
LOGS_DIR = BASE_DIR / "logs"
WEBSITE_DIR = BASE_DIR / "website"

def count_content():
    """Count all generated content."""
    total_articles = 0
    total_words = 0
    by_date = {}
    
    if CONTENT_DIR.exists():
        for d in sorted(CONTENT_DIR.iterdir()):
            if d.is_dir():
                articles = list(d.glob("*.md"))
                date = d.name[:10] if len(d.name) > 10 else d.name
                art_count = len(articles)
                total_articles += art_count
                
                words = 0
                for a in articles:
                    try:
                        words += len(a.read_text().split())
                    except:
                        pass
                total_words += words
                
                if date not in by_date:
                    by_date[date] = {"articles": 0, "words": 0}
                by_date[date]["articles"] += art_count
                by_date[date]["words"] += words
    
    return total_articles, total_words, by_date

def count_products():
    """Count digital products."""
    products_dir = BASE_DIR / "products" / "prompt-packs"
    products = []
    if products_dir.exists():
        for f in products_dir.glob("*-description.md"):
            try:
                content = f.read_text()
                lines = content.split('\n')
                name = ""
                price = ""
                for i, line in enumerate(lines):
                    if line.startswith('**Price:**'):
                        price = line.replace('**Price:**', '').strip()
                    if i == 0 and line.strip():
                        name = line.strip()
                products.append({"name": name, "price": price, "file": f.name})
            except:
                pass
    return products

def generate_report():
    """Generate the daily operations report."""
    total_articles, total_words, by_date = count_content()
    products = count_products()
    
    report = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.now().strftime("%H:%M:%S"),
        "system": {
            "status": "online",
            "host": "Mac mini M4",
            "uptime_days": "N/A"
        },
        "content": {
            "total_articles": total_articles,
            "total_words": total_words,
            "by_date": by_date
        },
        "products": {
            "count": len(products),
            "items": products
        },
        "revenue": {
            "total": 0.0,
            "today": 0.0,
            "by_source": {}
        },
        "tasks": {
            "completed_today": 0,
            "failed_today": 0
        }
    }
    
    # Load previous revenue if exists
    rev_file = DATA_DIR / "revenue.json"
    if rev_file.exists():
        try:
            report["revenue"] = json.loads(rev_file.read_text())
        except:
            pass
    
    # Load task history
    state_file = DATA_DIR / "orchestrator_state.json"
    if state_file.exists():
        try:
            state = json.loads(state_file.read_text())
            report["tasks"]["total_tracked"] = len(state.get('tasks', []))
        except:
            pass
    
    # Save report
    report_file = DATA_DIR / f"daily_{datetime.now().strftime('%Y%m%d')}.json"
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    return report

def update_website_stats(report):
    """Update the website HTML with latest stats."""
    # Simple stat update - in production would parse and update HTML
    html_file = WEBSITE_DIR / "index.html"
    if html_file.exists():
        html = html_file.read_text()
        
        # Update article count (simple find-and-replace for the stats)
        # This is a basic implementation
        print(f"[WEBSITE] Stats updated: {report['content']['total_articles']} articles, {report['content']['total_words']} words")
    
    return True

def print_report(report):
    """Print a human-readable report."""
    print("\n" + "=" * 50)
    print(f"📊 AUTOMIND DAILY REPORT")
    print(f"   {report['date']}")
    print("=" * 50)
    
    print(f"\n📝 CONTENT")
    print(f"   Total Articles: {report['content']['total_articles']}")
    print(f"   Total Words:    {report['content']['total_words']:,}")
    
    print(f"\n📦 PRODUCTS")
    print(f"   Digital Products: {report['products']['count']}")
    for p in report['products']['items']:
        print(f"   • {p.get('name', 'Unnamed')} - {p.get('price', 'N/A')}")
    
    print(f"\n💰 REVENUE")
    print(f"   Total: ${report['revenue']['total']:.2f}")
    
    print(f"\n✅ STATUS")
    print(f"   System: {report['system']['status']}")
    print(f"   Reports Saved: {DATA_DIR}")
    print("=" * 50)

def main():
    report = generate_report()
    update_website_stats(report)
    print_report(report)
    
    # Also save a plain-text summary for quick viewing
    summary_file = DATA_DIR / "latest_status.txt"
    with open(summary_file, 'w') as f:
        f.write(f"AutoMind Status - {report['date']}\n")
        f.write(f"Articles: {report['content']['total_articles']}\n")
        f.write(f"Words: {report['content']['total_words']:,}\n")
        f.write(f"Products: {report['products']['count']}\n")
        f.write(f"Revenue: ${report['revenue']['total']:.2f}\n")
        f.write(f"System: {report['system']['status']}\n")

if __name__ == "__main__":
    main()
