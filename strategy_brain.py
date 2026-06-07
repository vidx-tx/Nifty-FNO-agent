def run():
    return {
        "day": 1,
        "date": "2026-06-07",
        "mode": "PAPER_ONLY",
        "live_trading_enabled": False,
        "nifty_spot": 25000,
        "market_bias": "BULLISH",
        "suggested_instrument": "NIFTY CE",
        "strike_logic": "Prefer ATM or slightly ITM CE. Avoid far OTM CE.",
        "entry_zone": "Above 25100",
        "stop_loss": "Below 24900",
        "target": "25180 to 25250",
        "news_risk": "low",
        "final_decision": "PAPER_TRADE_ONLY",
        "reason": "Trend is bullish. Price is above VWAP. CE bias selected.",
        "win_rate": 0,
        "profit_factor": 0,
        "should_unlock_live_mode": False,
        "report_text": "📊 NIFTY F&O Paper Plan\n\nDay: 1\nMode: PAPER_ONLY\nLive Trading: LOCKED\n\nNIFTY Spot: 25000\nMarket Bias: BULLISH\nPreferred Side: NIFTY CE\nSuggested Strike: Prefer ATM or slightly ITM CE. Avoid far OTM CE.\n\nEntry Zone: Above 25100\nStop Loss: Below 24900\nTarget: 25180 to 25250\n\nNews Risk: low\nFinal Decision: PAPER_TRADE_ONLY\n\nReason: Trend is bullish. Price is above VWAP. CE bias selected.\n\nImportant: This is paper trade only. No live trade for the first 10 trading days."
    }
