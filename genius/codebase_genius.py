#!/usr/bin/env python3
"""
Codebase Genius - An Agentic Code Documentation System
Assignment 2: AI-Powered Autonomous Documentation Generator
"""

import os
import ast
import glob
import json
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime

class CodebaseGenius:
    """
    An intelligent agent that autonomously analyzes codebases 
    and generates comprehensive documentation.
    """
    
    def _init_(self):
        self.supported_extensions = ['.py', '.js', '.java', '.cpp', '.c', '.html', '.css', '.ts']
        self.analysis_results = {}
        self.agent_name = "🤖 Codebase Genius Agent"
        
    def agent_log(self, message: str):
        """Agent-style logging"""
        print(f"{self.agent_name}: {message}")
    
    def discover_code_files(self, directory: str = '.') -> List[str]:
        """Autonomously discover all code files in the project"""
        self.agent_log("Starting file discovery...")
        code_files = []
        
        for ext in self.supported_extensions:
            pattern = os.path.join(directory, '', f'*{ext}')
            found_files = glob.glob(pattern, recursive=True)
            code_files.extend(found_files)
            
        self.agent_log(f"Discovered {len(code_files)} code files")
        return code_files
    
    def analyze_python_file(self, filepath: str) -> Dict[str, Any]:
        """Intelligently analyze Python file structure and content"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            analysis = {
                'file_path': filepath,
                'file_name': os.path.basename(filepath),
                'line_count': len(content.split('\n')),
                'file_size': len(content),
                'functions': [],
                'classes': [],
                'imports': [],
                'analysis_timestamp': datetime.now().isoformat()
            }
            
            # Advanced AST parsing for intelligent analysis
            try:
                tree = ast.parse(content)
                
                for node in ast.walk(tree):
                    if isinstance(node, ast.FunctionDef):
                        func_analysis = {
                            'name': node.name,
                            'line': node.lineno,
                            'args': [arg.arg for arg in node.args.args],
                            'docstring': ast.get_docstring(node) or "No docstring"
                        }
                        analysis['functions'].append(func_analysis)
                        
                    elif isinstance(node, ast.ClassDef):
                        class_analysis = {
                            'name': node.name,
                            'line': node.lineno,
                            'methods': [],
                            'docstring': ast.get_docstring(node) or "No docstring"
                        }
                        analysis['classes'].append(class_analysis)
                        
                    elif isinstance(node, (ast.Import, ast.ImportFrom)):
                        for alias in node.names:
                            analysis['imports'].append(alias.name)
                            
            except SyntaxError as e:
                analysis['ast_error'] = f"Syntax error: {e}"
            
            return analysis
            
        except Exception as e:
            return {'file_path': filepath, 'error': str(e), 'status': 'failed'}
    
    def analyze_generic_file(self, filepath: str) -> Dict[str, Any]:
        """Analyze non-Python files with basic structure detection"""
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            lines = content.split('\n')
            
            # Basic pattern detection
            functions = []
            for i, line in enumerate(lines):
                if any(keyword in line for keyword in ['function ', 'def ', 'func ']):
                    functions.append({'line': i+1, 'content': line.strip()})
            
            return {
                'file_path': filepath,
                'file_name': os.path.basename(filepath),
                'line_count': len(lines),
                'file_size': len(content),
                'type': 'generic',
                'detected_patterns': functions,
                'analysis_timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            return {'file_path': filepath, 'error': str(e), 'status': 'failed'}
    
    def generate_project_intelligence(self, analyses: List[Dict]) -> Dict[str, Any]:
        """Generate intelligent insights about the entire codebase"""
        successful_analyses = [a for a in analyses if 'error' not in a]
        failed_analyses = [a for a in analyses if 'error' in a]
        
        total_functions = sum(len(a.get('functions', [])) for a in successful_analyses)
        total_classes = sum(len(a.get('classes', [])) for a in successful_analyses)
        total_lines = sum(a.get('line_count', 0) for a in successful_analyses)
        
        # Language distribution
        language_stats = {}
        for analysis in successful_analyses:
            ext = os.path.splitext(analysis['file_path'])[1]
            language_stats[ext] = language_stats.get(ext, 0) + 1
        
        return {
            'project_intelligence': {
                'total_files_analyzed': len(successful_analyses),
                'total_files_failed': len(failed_analyses),
                'total_lines_of_code': total_lines,
                'total_functions': total_functions,
                'total_classes': total_classes,
                'language_distribution': language_stats,
                'analysis_completed_at': datetime.now().isoformat(),
                'agent_version': '1.0.0'
            },
            'file_analyses': analyses
        }
    
    def generate_comprehensive_documentation(self, project_data: Dict[str, Any]) -> str:
        """Generate comprehensive Markdown documentation autonomously"""
        intelligence = project_data['project_intelligence']
        analyses = project_data['file_analyses']
        
        markdown = [
            "# 🤖 Codebase Genius - Automated Documentation",
            "",
            "> Generated autonomously by Codebase Genius Agent",
            "",
            "## 📊 Project Intelligence Report",
            "",
            f"- *Total Files Analyzed*: {intelligence['total_files_analyzed']}",
            f"- *Total Lines of Code*: {intelligence['total_lines_of_code']}",
            f"- *Functions Discovered*: {intelligence['total_functions']}",
            f"- *Classes Identified*: {intelligence['total_classes']}",
            f"- *Analysis Date*: {intelligence['analysis_completed_at']}",
            f"- *Agent Version*: {intelligence['agent_version']}",
            "",
            "## 🌐 Language Distribution",
            ""
        ]
        
        for lang, count in intelligence['language_distribution'].items():
            markdown.append(f"- {lang}: {count} files")
        
        markdown.extend([
            "",
            "## 📁 Detailed File Analysis",
            ""
        ])
        
        for analysis in analyses:
            if 'error' not in analysis:
                markdown.append(f"### 🔍 {analysis['file_name']}")
                markdown.append(f"- *Path*: {analysis['file_path']}")
                markdown.append(f"- *Lines*: {analysis['line_count']}")
                markdown.append(f"- *Size*: {analysis['file_size']} bytes")
                
                if analysis.get('functions'):
                    markdown.append("- *🧩 Functions*:")
                    for func in analysis['functions']:
                        markdown.append(f"  - {func['name']} (line {func['line']})")
                        if func['docstring'] and func['docstring'] != "No docstring":
                            markdown.append(f"    - {func['docstring']}")
                
                if analysis.get('classes'):
                    markdown.append("- *🏗 Classes*:")
                    for cls in analysis['classes']:
                        markdown.append(f"  - {cls['name']} (line {cls['line']})")
                        if cls['docstring'] and cls['docstring'] != "No docstring":
                            markdown.append(f"    - {cls['docstring']}")
                
                if analysis.get('imports'):
                    markdown.append("- *📦 Imports*:")
                    for imp in analysis['imports'][:10]:  # Show first 10 imports
                        markdown.append(f"  - {imp}")
                
                markdown.append("")
        
        if any('error' in a for a in analyses):
            markdown.extend([
                "## ⚠ Analysis Issues",
                ""
            ])
            for analysis in analyses:
                if 'error' in analysis:
                    markdown.append(f"- {analysis['file_path']}: {analysis['error']}")
        
        markdown.extend([
            "",
            "---",
            "Documentation generated autonomously by Codebase Genius Agent",
            ""
        ])
        
        return '\n'.join(markdown)
    
    def run_autonomous_analysis(self, directory: str = '.') -> Dict[str, Any]:
        """
        Main agent method - runs complete autonomous analysis
        This is where the 'agentic' behavior happens!
        """
        self.agent_log("🚀 Initializing autonomous code analysis...")
        self.agent_log(f"Target directory: {os.path.abspath(directory)}")
        
        # Autonomous file discovery
        files = self.discover_code_files(directory)
        
        if not files:
            self.agent_log("❌ No code files found!")
            return {'error': 'No code files discovered'}
        
        # Autonomous file analysis
        analyses = []
        for filepath in files:
            self.agent_log(f"🔍 Analyzing: {os.path.basename(filepath)}")
            
            if filepath.endswith('.py'):
                analysis = self.analyze_python_file(filepath)
            else:
                analysis = self.analyze_generic_file(filepath)
            
            analyses.append(analysis)
        
        # Generate intelligence
        project_data = self.generate_project_intelligence(analyses)
        
        # Autonomous documentation generation
        documentation = self.generate_comprehensive_documentation(project_data)
        
        # Save outputs
        output_files = self.save_analysis_outputs(project_data, documentation)
        
        self.agent_log("✅ Autonomous analysis completed successfully!")
        self.agent_log(f"📁 Generated files: {', '.join(output_files)}")
        
        return {
            'status': 'success',
            'project_intelligence': project_data['project_intelligence'],
            'generated_files': output_files
        }
    
    def save_analysis_outputs(self, project_data: Dict, documentation: str) -> List[str]:
        """Autonomously save all analysis outputs"""
        output_files = []
        
        # Save Markdown documentation
        with open('CODEBASE_GENIUS_DOCUMENTATION.md', 'w', encoding='utf-8') as f:
            f.write(documentation)
        output_files.append('CODEBASE_GENIUS_DOCUMENTATION.md')
        
        # Save raw analysis data (for potential AI training)
        with open('codebase_analysis.json', 'w', encoding='utf-8') as f:
            json.dump(project_data, f, indent=2)
        output_files.append('codebase_analysis.json')
        
        return output_files

def main():
    """Launch the Codebase Genius Agent"""
    print("=" * 60)
    print("🤖 CODEBASE GENIUS - Agentic Documentation System")
    print("=" * 60)
    
    genius = CodebaseGenius()
    
    # Run autonomous analysis
    result = genius.run_autonomous_analysis()
    
    print("\n" + "=" * 60)
    if result['status'] == 'success':
        print("🎉 MISSION ACCOMPLISHED!")
        print(f"📊 Files analyzed: {result['project_intelligence']['total_files_analyzed']}")
        print(f"📝 Documentation: {result['generated_files'][0]}")
        print("🚀 Your assignment is READY for submission!")
    else:
        print("❌ Analysis failed - check the errors above")
    print("=" * 60)

if _name_ == "_main_":
    main()
