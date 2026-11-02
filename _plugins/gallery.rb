# Sorts the gallery by the date written into each file name.
#
# Files are named `YYYY-MM-DD-name.webp`; that date is the source of truth for
# both the `// YYYY` heading and the order. When a file name carries no date the
# `taken` field from _data/gallery.yml is used instead, and entries with neither
# sort last.
#
# Order: newest year first, then newest month/day inside that year; photos on the
# same day keep their _data/gallery.yml order (the older addition stays on top).
module Gumezm
  module Gallery
    FILE_DATE = %r{/(\d{4}-\d{2}-\d{2})-[^/]+\.webp\z}.freeze

    module_function

    def photo_date(item)
      match = item["src"].to_s.match(FILE_DATE)
      return match[1] if match

      taken = item["taken"].to_s.strip
      match = taken.match(/\A(\d{4}-\d{2}-\d{2})/)
      match && match[1]
    end

    def sort_key(item, index)
      date = item["date"]
      return [1, 0, 0, 0, index] if date.nil?

      year, month, day = date.split("-").map(&:to_i)
      [0, -year, -month, -day, index]
    end

    def apply(site)
      items = site.data["gallery"]
      return unless items.is_a?(Array)

      items.each { |item| item["date"] = photo_date(item) }
      site.data["gallery"] = items.each_with_index.sort_by { |item, index| sort_key(item, index) }.map(&:first)
    end
  end
end

Jekyll::Hooks.register :site, :post_read do |site|
  Gumezm::Gallery.apply(site)
end
