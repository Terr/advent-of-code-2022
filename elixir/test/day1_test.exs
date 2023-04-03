defmodule Day1Test do
  use ExUnit.Case

  test "part 1" do
    assert Day1.solve("../puzzle-input/day1-example-input.txt") == 24_000
    assert Day1.solve("../puzzle-input/day1-input.txt") == 69_206
  end

  test "part 2" do
    assert Day1Part2.solve("../puzzle-input/day1-example-input.txt") == 45_000
    assert Day1Part2.solve("../puzzle-input/day1-input.txt") == 197_400
  end
end
