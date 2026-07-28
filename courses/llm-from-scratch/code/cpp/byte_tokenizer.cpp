#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

// Byte tokenizer giữ từng byte UTF-8 thành một token 0..255.
std::vector<std::uint8_t> encode(const std::string& text) {
    return std::vector<std::uint8_t>(text.begin(), text.end());
}

// Ghép byte theo đúng thứ tự để phục hồi chuỗi UTF-8 ban đầu.
std::string decode(const std::vector<std::uint8_t>& ids) {
    return std::string(ids.begin(), ids.end());
}

int main(int argc, char** argv) {
    const std::string text = argc > 1 ? argv[1] : "LLM tiếng Việt";
    const auto ids = encode(text);
    std::cout << "bytes=" << ids.size() << " ids=";
    for (const auto id : ids) std::cout << static_cast<int>(id) << ' ';
    std::cout << "\ndecoded=" << decode(ids) << '\n';
    return decode(ids) == text ? 0 : 1;
}
