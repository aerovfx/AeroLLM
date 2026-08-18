#include <fstream>
#include <iostream>
#include <set>
#include <sstream>
#include <string>

// Định dạng demo TSV: shard_id<TAB>token_count<TAB>sha256.
int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "usage: shard_manifest manifest.tsv\n";
        return 2;
    }
    std::ifstream input(argv[1]);
    if (!input) {
        std::cerr << "cannot open manifest\n";
        return 2;
    }
    std::set<std::string> seen;
    std::string line;
    std::uint64_t total_tokens = 0;
    std::size_t rows = 0;
    while (std::getline(input, line)) {
        std::istringstream row(line);
        std::string shard_id, token_text, sha256;
        if (!std::getline(row, shard_id, '\t') || !std::getline(row, token_text, '\t') ||
            !std::getline(row, sha256) || shard_id.empty() || sha256.size() != 64) {
            std::cerr << "invalid row " << rows + 1 << '\n';
            return 1;
        }
        if (!seen.insert(shard_id).second) {
            std::cerr << "duplicate shard_id: " << shard_id << '\n';
            return 1;
        }
        total_tokens += std::stoull(token_text);
        ++rows;
    }
    std::cout << "rows=" << rows << " total_tokens=" << total_tokens << '\n';
    return 0;
}
