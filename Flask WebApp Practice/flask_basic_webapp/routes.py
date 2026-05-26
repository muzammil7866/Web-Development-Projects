from flask import Blueprint, render_template, jsonify
from datetime import datetime

bp = Blueprint('main', __name__)


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html', now=datetime.utcnow())


@bp.route('/status')
def status():
    return jsonify({
        'status': 'ok',
        'timestamp': datetime.utcnow().isoformat() + 'Z'
    })
