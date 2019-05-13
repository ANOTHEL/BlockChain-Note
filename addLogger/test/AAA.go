package trie

import (
	mrand "math/rand"
	"time"
)

func init() {
	mrand.Seed(time.Now().Unix())
}

func (fb *filterBackend) BloomStatus() (uint64, uint64) { return 4096, 0 }
