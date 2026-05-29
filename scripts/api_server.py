#!/usr/bin/env python3
"""
AutoMind AI Content API Service
================================
A lightweight API service that provides AI-powered content generation.
Built with Python - can run locally on Mac mini, deployable to any server.

Usage:
  python3 api_server.py          # Start server on port 8080
  python3 api_server.py --port 9000  # Custom port

Endpoints:
  POST /generate    - Generate SEO content from topic
  POST /meta        - Generate SEO metadata
  GET  /status      - System status
  GET  /products    - Available products
"""

import json
import os
import sys
import argparse
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse, parse_qs

BASE_DIR = Path(__file__).parent.parent
CONTENT_DIR = BASE_DIR / "content" / "generated"
DATA_DIR = BASE_DIR / "data"

API_VERSION = "0.1.0"
API_NAME = "AutoMind Content API"

class ContentAPIHandler(BaseHTTPRequestHandler):
    
    def _send_json(self, data, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2, ensure_ascii=False).encode())
    
    def _read_body(self):
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length > 0:
            body = self.rfile.read(content_length)
            return json.loads(body)
        return {}
    
    def do_OPTIONS(self):
        self._send_json({})
    
    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path.rstrip('/')
        
        if path == '/status' or path == '':
            self._send_json({
                "api": API_NAME,
                "version": API_VERSION,
                "status": "online",
                "uptime": "24/7",
                "host": "Mac mini M4",
                "timestamp": datetime.now().isoformat()
            })
        
        elif path == '/products':
            products = []
            products_dir = BASE_DIR / "products" / "prompt-packs"
            if products_dir.exists():
                for f in products_dir.glob("*-description.md"):
                    try:
                        content = f.read_text()
                        name = f.name.replace("-description.md", "").replace("-", " ").title()
                        products.append({
                            "name": name,
                            "description_file": f.name,
                            "available": True
                        })
                    except:
                        pass
            
            self._send_json({
                "products": products,
                "count": len(products)
            })
        
        elif path.startswith('/content/'):
            # List or get content
            date_prefix = path.replace('/content/', '')
            if date_prefix:
                # Try to find specific content
                for d in sorted(CONTENT_DIR.iterdir(), reverse=True):
                    if date_prefix in d.name:
                        articles = list(d.glob("*.md"))
                        content_data = []
                        for article in articles:
                            content_data.append({
                                "file": str(article.relative_to(BASE_DIR)),
                                "size": article.stat().st_size,
                                "modified": datetime.fromtimestamp(article.stat().st_mtime).isoformat()
                            })
                        self._send_json({"date": d.name, "articles": content_data})
                        return
                self._send_json({"error": "Content not found"}, 404)
            else:
                # List all content directories
                dirs = sorted([d.name for d in CONTENT_DIR.iterdir() if d.is_dir()], reverse=True)
                self._send_json({"content_directories": dirs, "count": len(dirs)})
        
        else:
            self._send_json({"error": "Not found", "endpoints": ["/status", "/products", "/content/"]}, 404)
    
    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path.rstrip('/')
        
        if path == '/generate':
            body = self._read_body()
            topic = body.get('topic', '')
            keywords = body.get('keywords', [])
            
            if not topic:
                self._send_json({"error": "Topic is required"}, 400)
                return
            
            # Queue the generation request
            # (In production, this would trigger the AI content pipeline)
            request_id = datetime.now().strftime("%Y%m%d%H%M%S")
            
            # Save request to queue
            queue_file = DATA_DIR / "api_requests.json"
            requests = []
            if queue_file.exists():
                try:
                    requests = json.loads(queue_file.read_text())
                except:
                    requests = []
            
            requests.append({
                "id": request_id,
                "topic": topic,
                "keywords": keywords,
                "status": "queued",
                "created": datetime.now().isoformat()
            })
            
            queue_file.write_text(json.dumps(requests, indent=2, ensure_ascii=False))
            
            self._send_json({
                "success": True,
                "request_id": request_id,
                "message": f"Content generation queued for: {topic}",
                "status": "queued",
                "note": "AI will process this request. Check /content/ for results."
            })
        
        elif path == '/meta':
            body = self._read_body()
            topic = body.get('topic', '')
            
            if not topic:
                self._send_json({"error": "Topic is required"}, 400)
                return
            
            # Generate sample SEO metadata (AI-powered)
            # In production, this would use the AI model
            self._send_json({
                "topic": topic,
                "suggested_title": f"{topic}: Complete Guide & Best Practices (2026)",
                "meta_description": f"Discover everything about {topic}. Our comprehensive guide covers features, pricing, comparisons, and expert recommendations for 2026.",
                "seo_keywords": [topic, f"best {topic}", f"{topic} review", f"{topic} 2026", f"{topic} guide"],
                "status": "generated"
            })
        
        else:
            self._send_json({"error": "Not found", "available": ["/generate", "/meta"]}, 404)
    
    def log_message(self, format, *args):
        """Custom logging with timestamp."""
        print(f"[API] {datetime.now().strftime('%H:%M:%S')} {args[0]} {args[1]} {args[2]}")


def main():
    parser = argparse.ArgumentParser(description="AutoMind Content API Server")
    parser.add_argument('--port', type=int, default=8080, help='Port to listen on')
    parser.add_argument('--host', default='127.0.0.1', help='Host to bind to')
    args = parser.parse_args()
    
    server = HTTPServer((args.host, args.port), ContentAPIHandler)
    
    print(f"""
╔══════════════════════════════════════╗
║     AutoMind Content API Server     ║
║──────────────────────────────────────║
║  Version: {API_VERSION:<20}║
║  Host:    {args.host:<20}║
║  Port:    {args.port:<20}║
║  Status:  Running                    ║
║──────────────────────────────────────║
║  Endpoints:                          ║
║    GET  /status     - System status  ║
║    GET  /products   - List products  ║
║    GET  /content/   - View content   ║
║    POST /generate   - Generate       ║
║    POST /meta       - SEO metadata   ║
╚══════════════════════════════════════╝
    """)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[API] Shutting down...")
        server.server_close()


if __name__ == '__main__':
    main()
