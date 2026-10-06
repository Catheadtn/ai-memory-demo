import sys
sys.stdout.reconfigure(encoding='utf-8')
from mem0 import Memory

# ⚠️⚠️⚠️ 这里的 Key 换成你充过值的那个真实 Key！！！
MY_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "sk-.")

def init_memory():
    config = {
        "embedder": {
            "provider": "huggingface",
            "config": {"model": "all-MiniLM-L6-v2"}
        },
        "vector_store": {
            "provider": "qdrant",
            "config": {
                "collection_name": "mem0_test_384",
                "embedding_model_dims": 384
            }
        },
        "llm": {
            "provider": "deepseek",
            "config": {
                "model": "deepseek-chat",
                "api_key": MY_API_KEY
            }
        }
    }
    return Memory.from_config(config)

if __name__ == "__main__":
    print("正在初始化记忆系统...")
    mem = init_memory()

    user_name = input("请输入你的名字（或用户ID）: ")
    print(f"欢迎，{user_name}！")

    print("\n[1/2] 正在存储记忆...")
    mem.add(f"{user_name}正在学习AI记忆系统", user_id=user_name)
    mem.add("目标是找到一份AI开发工作", user_id=user_name)

    print("[2/2] 正在拉取所有记忆...")
    all_memories = mem.get_all(filters={"user_id": user_name})
    
    print("\n🔍 所有的记忆:")
    for item in all_memories.get("results", []):
        print(f"  - {item['memory']}")

    print("\n--- 程序结束 ---")