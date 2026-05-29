#!/usr/bin/env python3
"""
Auto Income - Content Generation Engine
Generates SEO-optimized affiliate content for multiple platforms.
This script creates structured content outlines that the AI agent fills in.
"""

import json
import os
from datetime import datetime
from pathlib import Path

BASE = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def load_affiliate_programs():
    with open(BASE / "affiliate" / "programs.json") as f:
        return json.load(f)

def generate_content_plan():
    """Generate a content plan for the next batch of articles."""
    programs = load_affiliate_programs()
    
    # Content topics based on high-commission programs
    topics = [
        {
            "id": "ai-writing-tools-comparison",
            "title_en": "Best AI Writing Tools in 2026: In-Depth Comparison & Review",
            "title_zh": "2026年最佳AI写作工具深度对比评测",
            "target_en": "Writesonic (30% recurring), Jasper (30%)",
            "target_zh": "AI写作工具评测（暂不区分佣金）",
            "type": "comparison",
            "word_count": 2500,
            "affiliates": ["Writesonic", "Jasper AI", "Semrush"],
            "platforms": ["medium", "zhihu", "blog"],
            "seo_keywords": ["best AI writing tools", "AI writing software review", "Writesonic vs Jasper"]
        },
        {
            "id": "web-hosting-for-beginners",
            "title_en": "Best Web Hosting for Beginners 2026: Affordable & Reliable Options",
            "title_zh": "2026年新手建站推荐：最值得入门的虚拟主机",
            "target_en": "Hostinger (60% first purchase)",
            "target_zh": "建站服务推荐",
            "type": "review",
            "word_count": 2000,
            "affiliates": ["Hostinger", "Cloudways"],
            "platforms": ["medium", "blog"],
            "seo_keywords": ["best web hosting 2026", "affordable hosting", "Hostinger review"]
        },
        {
            "id": "seo-tools-guide",
            "title_en": "Semrush vs Ahrefs vs Moz: Which SEO Tool Should You Choose in 2026?",
            "title_zh": "Semrush vs Ahrefs vs Moz：2026年SEO工具终极对比",
            "target_en": "Semrush (40% first purchase)",
            "target_zh": "SEO工具对比",
            "type": "comparison",
            "word_count": 3000,
            "affiliates": ["Semrush"],
            "platforms": ["medium", "zhihu", "blog"],
            "seo_keywords": ["Semrush review", "best SEO tool 2026", "SEO tool comparison"]
        },
        {
            "id": "ai-image-generation",
            "title_en": "Best AI Image Generators in 2026: From Midjourney to DALL-E 3",
            "title_zh": "2026年最佳AI图像生成工具全面评测",
            "target_en": "Canva ($36/referral)",
            "target_zh": "AI绘图工具评测",
            "type": "review",
            "word_count": 2500,
            "affiliates": ["Canva"],
            "platforms": ["medium", "zhihu", "xiaohongshu"],
            "seo_keywords": ["best AI image generator", "Midjourney alternative", "AI art tools 2026"]
        },
        {
            "id": "small-business-email-marketing",
            "title_en": "Email Marketing for Small Business: Best Tools & Strategies 2026",
            "title_zh": "小企业邮件营销指南：2026年最佳工具与策略",
            "target_en": "ConvertKit (30% recurring)",
            "target_zh": "邮件营销工具",
            "type": "guide",
            "word_count": 2000,
            "affiliates": ["ConvertKit"],
            "platforms": ["medium", "blog"],
            "seo_keywords": ["email marketing tools", "ConvertKit review", "small business email"]
        },
        {
            "id": "ecommerce-platforms",
            "title_en": "Shopify vs WooCommerce vs BigCommerce: Which is Best in 2026?",
            "title_zh": "Shopify vs WooCommerce vs BigCommerce：2026年电商平台对比",
            "target_en": "Shopify ($58/referral)",
            "target_zh": "电商平台对比",
            "type": "comparison",
            "word_count": 3000,
            "affiliates": ["Shopify"],
            "platforms": ["medium", "zhihu", "blog"],
            "seo_keywords": ["Shopify review", "best ecommerce platform", "Shopify vs WooCommerce"]
        }
    ]
    
    return topics

def save_content_plan(topics):
    """Save the content plan for tracking."""
    output = BASE / "data" / "content_plan.json"
    plan = {
        "generated_at": datetime.now().isoformat(),
        "total_topics": len(topics),
        "topics": topics
    }
    with open(output, "w") as f:
        json.dump(plan, f, indent=2, ensure_ascii=False)
    print(f"[CONTENT PLAN] Saved {len(topics)} topics to {output}")
    return output

def generate_article_outline(topic):
    """Generate a structured outline for an article."""
    outline = {
        "meta": {
            "id": topic["id"],
            "title_en": topic["title_en"],
            "title_zh": topic["title_zh"],
            "type": topic["type"],
            "word_count": topic["word_count"],
            "target_affiliates": topic["affiliates"],
            "seo_keywords": topic["seo_keywords"]
        },
        "sections": [
            {"heading": "Introduction / 引言", "purpose": "Hook reader, state the problem this article solves"},
            {"heading": "Why This Matters / 为什么重要", "purpose": "Establish context and reader pain points"},
            {"heading": "Top Recommendations / 推荐列表", "purpose": "Main content - compare/review options"},
            {"heading": "Detailed Comparison / 详细对比", "purpose": "Feature-by-feature comparison table or analysis"},
            {"heading": "Pricing / 价格对比", "purpose": "Cost breakdown and value analysis"},
            {"heading": "Who Should Choose What / 如何选择", "purpose": "Decision guide based on use case"},
            {"heading": "Final Verdict / 最终结论", "purpose": "Summary and recommendation"},
            {"heading": "FAQs / 常见问题", "purpose": "Address common reader questions"}
        ],
        "affiliate_disclosure": "This article contains affiliate links. If you purchase through these links, we may earn a commission at no extra cost to you."
    }
    return outline

def build_content_directory(article_id, content_type="article"):
    """Create the directory structure for content."""
    today = datetime.now().strftime("%Y-%m-%d")
    dir_path = BASE / "content" / "generated" / f"{today}_{article_id}"
    dir_path.mkdir(parents=True, exist_ok=True)
    return dir_path

if __name__ == "__main__":
    print("=" * 60)
    print("AUTO INCOME - CONTENT GENERATION ENGINE")
    print("=" * 60)
    
    topics = generate_content_plan()
    save_content_plan(topics)
    
    for topic in topics:
        outline = generate_article_outline(topic)
        dir_path = build_content_directory(topic["id"])
        
        # Save outline
        outline_path = dir_path / "outline.json"
        with open(outline_path, "w") as f:
            json.dump(outline, f, indent=2, ensure_ascii=False)
        
        print(f"\n[OUTLINE] Created for: {topic['title_en']}")
        print(f"  Directory: {dir_path}")
        print(f"  Affiliates: {', '.join(topic['affiliates'])}")
        print(f"  Platforms: {', '.join(topic['platforms'])}")
    
    print(f"\n{'=' * 60}")
    print(f"Total articles planned: {len(topics)}")
    print(f"Next step: AI agent generates full article content for each outline")
